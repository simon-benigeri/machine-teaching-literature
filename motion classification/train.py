from argparse import ArgumentParser
from pathlib import Path
from typing import Optional

import numpy as np

from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer, TrainingArguments
# from datasets import load_metric
from sklearn.metrics import accuracy_score, balanced_accuracy_score, f1_score, classification_report

from dataset import setup_dataset
from load_docket_entries_dataset import load_dataset
from snorkel_labeling import create_lf_set, apply_lfs, LfAggregator, TieBreakPolicy


def compute_metrics(eval_preds):
    logits, targets = eval_preds
    outputs = np.argmax(logits, axis=-1)
    accuracy = accuracy_score(targets, outputs)
    balanced_accuracy = balanced_accuracy_score(targets, outputs)
    f1_score_micro = f1_score(targets, outputs, average='micro')
    f1_score_macro = f1_score(targets, outputs, average='macro')
    return {
        "accuracy": accuracy,
        "balanced_accuracy": balanced_accuracy,
        "f1_score_micro": f1_score_micro,
        "f1_score_macro": f1_score_macro
    }


def main(
        input_data: Path,
        output_data: Optional[Path],
        test_size: float,
        aggregator: LfAggregator,
        return_probs: bool,
        tie_break: TieBreakPolicy,
        epochs: int,
        batch_size: int
):
    # load dataset
    df_train, df_test = load_dataset(input_data=input_data,
                                     test_size=test_size,
                                     output_data=output_data)
    # create lfs
    lf_set = create_lf_set()

    # load tokenizer
    tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")
    # tokenizer = DistilBertTokenizer.from_pretrained("distilbert-base-uncased")

    # apply lfs to create training set
    train_texts, train_labels = apply_lfs(df_train=df_train,
                                          lfs=lf_set,
                                          aggregator=aggregator,
                                          return_probs=return_probs,
                                          tie_break_policy=tie_break)

    # format test set
    test_texts, test_labels = df_test['text'].tolist(), df_test['motion'].to_numpy(dtype=int)

    # train_dataset, val_dataset, test_dataset = setup_dataset(train_texts=train_texts,
    #                                                          train_labels=train_labels,
    #                                                          test_texts=test_texts,
    #                                                          test_labels=test_labels,
    #                                                          tokenizer=tokenizer)

    train_dataset, test_dataset = setup_dataset(train_texts=train_texts,
                                                train_labels=train_labels,
                                                test_texts=test_texts,
                                                test_labels=test_labels,
                                                tokenizer=tokenizer)

    training_args = TrainingArguments(
        output_dir='./results',  # output directory
        num_train_epochs=epochs,  # total number of training epochs
        per_device_train_batch_size=batch_size,  # batch size per device during training
        per_device_eval_batch_size=64,  # batch size for evaluation
        warmup_steps=500,  # number of warmup steps for learning rate scheduler
        weight_decay=0.01,  # strength of weight decay
        logging_dir='./logs',  # directory for storing logs
        logging_steps=10,
    )

    # print(train_labels[0])
    # config = AutoConfig.from_pretrained("distilbery-base-uncased")

    model = AutoModelForSequenceClassification.from_pretrained("distilbert-base-uncased")
    # model = DistilBertForSequenceClassification.from_pretrained("distilbert-base-uncased")
    
    if return_probs:
        model.config.problem_type = "multi_label_classification"
    else:
        model.config.problem_type = "single_label_classification"

    trainer = Trainer(
        model=model,  # the instantiated 🤗 Transformers model to be trained
        args=training_args,  # training arguments, defined above
        train_dataset=train_dataset,  # training dataset
        eval_dataset=test_dataset,  # evaluation dataset,
        compute_metrics=compute_metrics
    )

    trainer.train()

    performance = trainer.evaluate()
    print(performance)



if __name__ == '__main__':
    parser = ArgumentParser(description='This script trains a DistilBERT classifier on a weakly supervised dataset')
    parser.add_argument('--input-data', type=Path, default='data/court_docket_entries')
    parser.add_argument('--output-data', type=Path, nargs='?')
    parser.add_argument('--test-size', type=float, default=0.4)
    parser.add_argument('--aggregator', type=LfAggregator, default='majority-vote')
    parser.add_argument('--return-probs', default=False, action='store_true')
    parser.add_argument('--tie-break', type=TieBreakPolicy, default='abstain')
    parser.add_argument('--epochs', type=int, default=3)
    parser.add_argument('--batch-size', type=int, default=16)
    args = parser.parse_args()
    # print(dict(args._get_kwargs()))
    main(**dict(args._get_kwargs()))
