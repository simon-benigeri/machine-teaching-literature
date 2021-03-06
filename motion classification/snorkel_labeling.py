from typing import List
from enum import Enum

import numpy as np
import pandas as pd

from snorkel.labeling import filter_unlabeled_dataframe, LabelingFunction, PandasLFApplier
from snorkel.labeling.model.label_model import LabelModel
from snorkel.labeling.model.baselines import MajorityLabelVoter
from snorkel.utils import probs_to_preds

from labeling_functions.heuristics import lf_set_heuristics
from labeling_functions.keywords import lf_set_keywords
from labeling_functions.missing_keywords import lf_set_missing_keywords

# Set voting values.
ABSTAIN = -1
MOTION = 1
NOT_MOTION = 0


class ClassLabels(int, Enum):
    ABSTAIN = -1
    MOTION = 1
    NOT_MOTION = 0


class LfAggregator(str, Enum):
    MAJORITY_VOTE = 'majority-vote'
    LABEL_MODEL = 'label-model'


class TieBreakPolicy(str, Enum):
    RANDOM = 'random'
    TRUE_RANDOM = 'true-random'
    ABSTAIN = 'abstain'


def create_lf_set():
    return lf_set_heuristics + lf_set_keywords + lf_set_missing_keywords


def train_label_model(L_train: np.ndarray,
                      aggregator: LfAggregator):
    """

    :param L_train:
    :param aggregator:
    :return:
    """
    if aggregator == 'majority-vote':
        model = MajorityLabelVoter(cardinality=2)
    else:
        model = LabelModel(cardinality=2, device='cpu', verbose=True)
        model.fit(L_train=L_train, n_epochs=500, log_freq=100)

    return model


def apply_lfs(df_train: pd.DataFrame,
              lfs: List[LabelingFunction],
              aggregator: LfAggregator,
              return_probs: bool,
              tie_break_policy: TieBreakPolicy):
    """
    :param df_train:
    :param lfs:
    :param aggregator:
    :param return_probs:
    :param tie_break_policy:
    :return:
    """
    applier = PandasLFApplier(lfs=lfs)
    # L_train is label function predictions so [ lf_1(x),  lf_2(x), ... ] for all x in train set
    L_train = applier.apply(df=df_train)

    # Some line to analyze lfs
    # LFAnalysis(L=L_train, lfs=lfs).lf_summary(Y=dataset['motion'].to_numpy())
    # LFAnalysis(L=L_train, lfs=lfs).label_coverage()

    # Fit a label model
    label_model = train_label_model(L_train=L_train, aggregator=aggregator)

    # Predict probs labels
    preds_train = label_model.predict_proba(L=L_train)

    # Filter out examples not covered by any labeling function
    df_train_filtered, preds_train_filtered = filter_unlabeled_dataframe(X=df_train, y=preds_train, L=L_train)

    texts, snorkel_labels = df_train_filtered['text'].to_numpy(dtype=str), preds_train_filtered

    #TODO: WILL THIS BREAK IF I USE ABSTAIN WITH PROBABILISTIC LABELS?

    # create a boolean mask to eventually remove samples with ABSTAIN
    mask = np.full((len(snorkel_labels), ), True, dtype=bool)

    # Convert prob labels to predictions
    if not return_probs:
        snorkel_labels = probs_to_preds(probs=snorkel_labels, tie_break_policy=tie_break_policy)

        if tie_break_policy == TieBreakPolicy.ABSTAIN:
            mask = snorkel_labels != ClassLabels.ABSTAIN

    return texts[mask].tolist(), snorkel_labels[mask]


if __name__=="__main__":
    from load_docket_entries_dataset import load_dataset
    #TODO: for 'majority-vote' and 'abstain' check values
    aggregator = LfAggregator.LABEL_MODEL
    return_probs=False
    tie_break = TieBreakPolicy.ABSTAIN
    df_train, df_test = load_dataset(input_data='data/court_docket_entries',
                                     test_size=0.4)
    # create lfs
    lf_set = create_lf_set()

    # apply lfs to create training set
    train_texts, train_labels = apply_lfs(df_train=df_train,
                                          lfs=lf_set,
                                          aggregator=aggregator,
                                          return_probs=return_probs,
                                          tie_break_policy=tie_break)

    # print(train_labels[0].shape)
    # if not return_probs: "Motion to blah", 1
    # if return probs: "Motion to blah", [0.0, 1.0]

    for i, x in enumerate(zip(train_texts, train_labels)):
        print(x[1])
        if i > 4:
            break