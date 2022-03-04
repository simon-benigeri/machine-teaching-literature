from typing import Optional
from pathlib import Path
import pandas as pd
from sklearn.model_selection import train_test_split


def load_dataset(input_data: Path = 'data/court_docket_entries',
                 test_size: float = 0.4,
                 output_data: Optional[Path] = None):
    """
    An ugly function to create the csv datasets for this project.
    :param input_data: court docket entries data (various csv files)
    :param output_data: where we save the output csv files
    :param test_size: test_size for train/test split
    :param save_data: save dataset
    :return:
    """
    # read entries, keep relevant columns, change column names
    entries = pd.read_csv(f"{input_data}/motionEntries.csv")
    entries_columns = ['id', 'text', 'case_id', 'sealed', 'jurisdiction']
    entries = entries[entries_columns].rename(columns={"id": "docket_entry_id"})

    # read tags, keep relevant columns, change column names
    tags = pd.read_csv(f"{input_data}/tags.csv")
    tags_columns = ['id', 'label']
    tags = tags[tags_columns].rename(columns={'id': 'tag_id'})
    tags['motion'] = tags['tag_id'].apply(lambda x: int(x not in [26, 28]))

    # read usertags, keep relevant columns, change column names
    usertags = pd.read_csv(f"{input_data}/usertags.csv")
    usertags_columns = ['id', 'docket_entry_id', 'tag_id']
    usertags = usertags[usertags_columns].rename(columns={'id': 'usertags_id'})

    # merge tags to get labels
    labels = pd.merge(usertags, tags, on='tag_id')

    # merge labels and entries to get docket entries and their labels
    labeled_motions = pd.merge(labels, entries, on='docket_entry_id')

    # remove entries with label "SKIP"
    labeled_motions = labeled_motions[labeled_motions['label'] != 'SKIP']

    keep_columns = ['docket_entry_id', 'motion', 'text']
    df = labeled_motions[keep_columns]

    df_train, df_test = train_test_split(df, test_size=test_size)

    if output_data:
        output_data.mkdir(parents=True, exist_ok=True)
        df_train.to_csv(f"{output_data}/train.csv", index=False)
        df_test.to_csv(f"{output_data}/test.csv", index=False)

    return df_train, df_test

