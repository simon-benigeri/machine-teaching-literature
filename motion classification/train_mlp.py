from argparse import ArgumentParser
from pathlib import Path
from random import shuffle
import shutil
from typing import Optional
from tqdm.notebook import trange, tqdm
import time
import json

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

import torch.nn as nn
import torch.nn.functional as F
from torch.utils.data import DataLoader
import torch.optim as optim
from dataset import MotionDatasetMLP
from load_docket_entries_dataset import load_dataset
from snorkel_labeling import create_lf_set, apply_lfs, LfAggregator, TieBreakPolicy

# TODO: Check out this article
# https://www.watchful.io/resources/working-with-probabilistic-data-labels-to-train-a-classifier

class MLP(nn.Module):
    def __init__(self, input_dim, output_dim):
        super().__init__()

        self.input_fc = nn.Linear(input_dim, 10000)
        self.hidden_fc = nn.Linear(10000, 2000)
        self.hidden_fc = nn.Linear(2000, 100)
        self.output_fc = nn.Linear(100, output_dim)

    def forward(self, x):

        # x = [batch size, height, width]

        batch_size = x.shape[0]

        x = x.view(batch_size, -1)

        # x = [batch size, height * width]

        h_1 = F.relu(self.input_fc(x))

        # h_1 = [batch size, 250]

        h_2 = F.relu(self.hidden_fc(h_1))

        # h_2 = [batch size, 100]

        y_pred = self.output_fc(h_2)

        # y_pred = [batch size, output dim]

        return y_pred, h_2

def calculate_accuracy(y_pred, y):
    top_pred = y_pred.argmax(1, keepdim=True)
    correct = top_pred.eq(y.view_as(top_pred)).sum()
    acc = correct.float() / y.shape[0]
    return acc

def train(model, iterator, optimizer, criterion, device):

    epoch_loss = 0
    epoch_acc = 0

    model.train()

    for (x, y) in tqdm(iterator, desc="Training", leave=False):

        x = x.to(device)
        y = y.to(device)

        optimizer.zero_grad()

        y_pred, _ = model(x)

        loss = criterion(y_pred, y)

        acc = calculate_accuracy(y_pred, y)

        loss.backward()

        optimizer.step()

        epoch_loss += loss.item()
        epoch_acc += acc.item()

    return epoch_loss / len(iterator), epoch_acc / len(iterator)

def main(
    input_data: Path,
    output_data: Optional[Path],
    test_size: float,
    aggregator: LfAggregator,
    return_probs: bool,
    tie_break: TieBreakPolicy,
    epochs: int,
    batch_size: int,
    eval_batch_size: int,
    debug: bool,
    ):

    # load dataset
    df_train, df_test = load_dataset(
        input_data=input_data, test_size=test_size, output_data=output_data
    )

    # create lfs
    lf_set = create_lf_set()


    # apply lfs to create training set
    train_texts, train_labels = apply_lfs(
        df_train=df_train,
        lfs=lf_set,
        aggregator=aggregator,
        return_probs=return_probs,
        tie_break_policy=tie_break,
    )

    # format test set
    test_texts, test_labels = (
        df_test["text"].tolist(),
        df_test["motion"].to_numpy(dtype=int),
    )

    # small sample for debugging
    if debug:
        train_texts = train_texts[:32]
        train_labels = train_labels[:32]
        test_texts = test_texts[:32]
        test_labels = test_labels[:32]

    # Extract features with tfidf
    vectorizer_tfidf = TfidfVectorizer(ngram_range=(1, 5))
    X_train = vectorizer_tfidf.fit_transform(train_texts).toarray().astype(np.float32)
    X_test = vectorizer_tfidf.transform(test_texts).toarray().astype(np.float32)
    # print(len(X_train[2]))
    # print(X_train.shape)
    # Create dataset
    train_dataset = MotionDatasetMLP(X_train, train_labels)
    # val_dataset = MOTIONSDataset(X_val, val_labels)
    test_dataset = MotionDatasetMLP(X_test, test_labels)

    # Probaly need some dataloader stuff here
    train_dataloader = DataLoader(train_dataset, batch_size=32, shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size=32, shuffle=True)

    data, label = next(iter(train_dataloader))
    print(data.shape, label.shape)

    # if we work with probabilistic labels
    if return_probs:
        # use loss/criterion = KL Div
        pass
    else:
        # use BCE
        loss = nn.BCELoss()

    model = MLP
    INPUT_DIM = 138443
    OUTPUT_DIM = 1

    model = MLP(INPUT_DIM, OUTPUT_DIM)
    optimizer = optim.Adam(model.parameters())
    # train loop
    EPOCHS = 10

    best_valid_loss = float('inf')

    for epoch in trange(EPOCHS):

        start_time = time.monotonic()
        train_loss, train_acc = train(model, train_dataloader, optimizer, loss, device="cpu")
        # valid_loss, valid_acc = evaluate(model, valid_iterator, criterion, device)

        # if valid_loss < best_valid_loss:
        #     best_valid_loss = valid_loss
            # torch.save(model.state_dict(), 'tut1-model.pt')

        end_time = time.monotonic()
        elapsed_time = end_time - start_time
        elapsed_mins = int(elapsed_time / 60)
        elapsed_secs = int(elapsed_time - (elapsed_mins * 60))

        print(f'Epoch: {epoch+1:02} | Epoch Time: {elapsed_mins}m {elapsed_secs}s')
        print(f'\tTrain Loss: {train_loss:.3f} | Train Acc: {train_acc*100:.2f}%')
        # print(f'\t Val. Loss: {valid_loss:.3f} |  Val. Acc: {valid_acc*100:.2f}%')
    # eval loop



if __name__ == "__main__":
    parser = ArgumentParser(
        description="This script trains a DistilBERT classifier on a weakly supervised dataset"
    )
    parser.add_argument("--input-data", type=Path, default="data/court_docket_entries")
    parser.add_argument("--output-data", type=Path, nargs="?")
    parser.add_argument("--test-size", type=float, default=0.4)
    parser.add_argument("--aggregator", type=LfAggregator, default="majority-vote")
    parser.add_argument("--return-probs", default=False, action="store_true")
    parser.add_argument("--tie-break", type=TieBreakPolicy, default="abstain")
    parser.add_argument("--epochs", type=int, default=3)
    parser.add_argument("--batch-size", type=int, default=16)
    parser.add_argument("--eval-batch-size", type=int, default=64)
    parser.add_argument("--debug", type=bool, default=False)
    args = parser.parse_args()
    # print(dict(args._get_kwargs()))
    main(**dict(args._get_kwargs()))