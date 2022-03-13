from argparse import ArgumentParser
from pathlib import Path
from typing import Optional
from tqdm import tqdm
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
        self.linear_1 = nn.Linear(input_dim, 256, bias=True)
        self.hidden_1 = nn.Linear(256, 128, bias=True)
        self.hidden_2 = nn.Linear(128, 64, bias=True)
        self.output = nn.Linear(64, output_dim)

    def forward(self, x):
        # x = [batch size, height, width]

        x = F.relu(self.linear_1(x))
        x = F.relu(self.hidden_1(x))
        x = F.relu(self.hidden_2(x))
        return self.output(x)

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
        y_pred = model(x)
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
    vectorizer_tfidf = TfidfVectorizer(ngram_range=(1, 2), max_features=2000)
    X_train = vectorizer_tfidf.fit_transform(train_texts).toarray().astype(np.float32)
    X_test = vectorizer_tfidf.transform(test_texts).toarray().astype(np.float32)
    # print(len(X_train[2]))
    # print(X_train.shape)
    # Create dataset
    train_dataset = MotionDatasetMLP(X_train, train_labels)
    # val_dataset = MOTIONSDataset(X_val, val_labels)
    test_dataset = MotionDatasetMLP(X_test, test_labels)

    # Probaly need some dataloader stuff here
    train_dataloader = DataLoader(train_dataset, batch_size=batch_size, shuffle=True)
    test_dataloader = DataLoader(test_dataset, batch_size=batch_size, shuffle=True)

    data, label = next(iter(train_dataloader))
    # if we work with probabilistic labels
    if return_probs:
        # use loss/criterion = KL Div
        # loss = nn.BCELoss()
        pass
    else:
        # use BCE
        loss = nn.BCELoss()

    model = MLP
    INPUT_DIM = train_dataset.data.shape[1] # * batch_size
    OUTPUT_DIM = 1

    model = MLP(INPUT_DIM, OUTPUT_DIM)
    optimizer = optim.Adam(model.parameters())
    # train loop
    EPOCHS = 10

    best_valid_loss = float('inf')

    for epoch in tqdm(range(EPOCHS)):

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