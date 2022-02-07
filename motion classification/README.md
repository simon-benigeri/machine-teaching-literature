# motion classification
Classifying court docket entries with snorkel.

## Directories and files

### snorkel_introduction.md
Some notes introducting Snorkel.
**Status: IN PROGRESS. NEED TO MOVE NOTES FROM DIFFERENT PLACES INTO ONE FILE**

### motion_classification_introduction.md
Some notes introducting the motion classification task with Snorkel.
**Status: IN PROGRESS. NEED TO MOVE NOTES FROM DIFFERENT PLACES INTO ONE FILE**

### motion_classification_final_comments.md
Some notes discussing future improvements or necessary functionalities to build a machine teaching system for motion classification with Snorkel. 
**Status: IN PROGRESS. NEED TO MOVE NOTES FROM DIFFERENT PLACES INTO ONE FILE**

### [binary__baseline.ipynb](https://github.com/simon-benigeri/machine-teaching-literature/blob/main/motion%20classification/binary__baseline.ipynb)

A notebook showing how to train a classifier for `MOTION` and `NOT MOTION` with Snorkel.

The notebook contains:
  - code to explore the data
  - code to create certain types labeling functions
  - code to make the definition of labeling functions more accessible to non-technical users
  - code to analyze the labeling functions
  - code to train a label model with Snorkel. This aggregates the labeling functions.
  - code to programmatically label the dataset with the label model. This can be done with hard or soft (probabilistic) labels.
  - code to train and evaluate a basic text classifier on the programmatically labeled data.
  - comments on problems encountered along the way, and some solutions.
  - comments on how to order all of these functionalities so as to define an interaction for the user to create a good labeling function set.

#### STATUS: IN PROGRESS

#### TO DO:
1. Train model on probabilistic labels. **EASY**
2. Move notes in this notebook to `snorkel_introduction.md` and `motion_classification_introduction`. **EASY**
3. Heuristic based labeling functions are important but the technical barrier to creating them is too high. Find a way to make this simpler. **HARD**


### multiclass__baseline.ipynb
A notebook showing how to train a classifier for types of `MOTION` with Snorkel.

#### STATUS: NOT STARTED YET
#### TO DO:
1. Create labeling functions for multiple classes.
2. Train and evaluate resulting classifiers.
3. Show how to deal with concept drift:
  - Case 1: add a class.
  - Case 2: combine two classes into one.
  - Case 3: split one class into two.

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

