from argparse import ArgumentParser
from pathlib import Path
from typing import Optional
import time
import json

import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer

from dataset import MOTIONSDataset
from load_docket_entries_dataset import load_dataset
from snorkel_labeling import create_lf_set, apply_lfs, LfAggregator, TieBreakPolicy

# TODO: Check out this article
# https://www.watchful.io/resources/working-with-probabilistic-data-labels-to-train-a-classifier

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
    X_train = vectorizer_tfidf.fit_transform(train_texts)
    X_test = vectorizer_tfidf.transform(test_texts)

    # Create dataset
    train_dataset = MOTIONSDataset(X_train, train_labels)
    # val_dataset = MOTIONSDataset(X_val, val_labels)
    test_dataset = MOTIONSDataset(X_test, test_labels)

    # Probaly need some dataloader stuff here

    # if we work with probabilistic labels
    if return_probs:
        # use loss/criterion = KL Div
    else:
        # use BCE

    # model = MLP

    # train loop

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
    args = parser.parse_args()
    # print(dict(args._get_kwargs()))
    main(**dict(args._get_kwargs()))
