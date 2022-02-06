# motion classification
Classifying court docket entries with snorkel

## Directories and files

### snorkel_introduction.md
Some notes introducting Snorkel.

### motion_classification_introduction.md
Some notes introducting the motion classification task with Snorkel.

### binary__baseline.ipynb
A notebook showing how to train a classifier for `MOTION` and `NOT MOTION` with Snorkel.

The notebook contains:
  - code to explore the data
  - code to create certain types labeling functions
  - code to make the definition of labeling functions more accessible to non-technical users
  - code to analyze the labeling functions
  - code to train a label model with Snorkel. This aggregates the labeling functions.
  - code to programmatically label the dataset with the label model. This can be done with hard or soft (probabilistic) labels.
  - code to train and evaluate a basic text classifier on the programmatically labeled data.
  - some comments on problems encountered along the way, and some solutions.
  - come comments on how to order all of these functionalities so as to define an interaction for the user to define good labeling functions.

### multiclass__baseline.ipynb
A notebook showing how to train a classifier for types of `MOTION` with Snorkel.
This notebook is not complete yet.

## Setup

### 1. Get the data
1. Download the court docket entries data
2. Create a directory called `court_docket_entries`
3. In this directory, move the files:
  - `motionEntries.csv`
  - `tags.csv`
  - `thingy.csv`
  - `users.csv`
  - `usertags.csv`

### 2. Create an environment
```
conda env create -f environment.yml
conda activate motion-classification
```

### 3. Open/run the notebooks
In your environment, run `jupyter lab`

