from typing import List

import numpy as np
import torch
from torch.utils.data import Dataset
from sklearn.model_selection import train_test_split

from transformers import DistilBertTokenizer


class MOTIONSDataset(Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels

    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item

    def __len__(self):
        return len(self.labels)


def setup_dataset(train_texts: List[str],
                  train_labels: np.array,
                  test_texts: List[str],
                  test_labels: np.array,
                  tokenizer: DistilBertTokenizer):
    """
    :param train_texts:
    :param train_labels:
    :param test_texts:
    :param test_labels:
    :param tokenizer:
    :return:
    """
    # train_texts, val_texts, train_labels, val_labels = train_test_split(train_texts, train_labels, test_size=.2)

    train_encodings = tokenizer(train_texts, truncation=True, padding=True)
    # val_encodings = tokenizer(val_texts, truncation=True, padding=True)
    test_encodings = tokenizer(test_texts, truncation=True, padding=True)

    train_dataset = MOTIONSDataset(train_encodings, train_labels)
    # val_dataset = MOTIONSDataset(val_encodings, val_labels)
    test_dataset = MOTIONSDataset(test_encodings, test_labels)

    # return train_dataset, val_dataset, test_dataset
    return train_dataset, test_dataset
