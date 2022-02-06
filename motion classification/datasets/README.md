# Datasets and tasks

## Text Classification

### 1. Antisemitic tweets
Source: Building NLP Classifiers Cheaply With Transfer Learning and Weak Supervision 
- [Medium blog post](https://medium.com/sculpt/a-technique-for-building-nlp-classifiers-efficiently-with-transfer-learning-and-weak-supervision-a8e2f21ca9c8)
- [paper](https://web.stanford.edu/class/archive/cs/cs224n/cs224n.1194/reports/custom/15577251.pdf)

#### Overview

*Dataset*: 26000 tweets that mention "jew", 700 labeled tweets to evaluate LFs, 450 labeled tweets to test the model

*Goal*: Build a large training set
Training a weak supervision model with SNORKEL

1. create LFs
2. train a generative model
3. create probabilistic training data
4. train a discriminative model

<img width="780" alt="Screen Shot 2021-10-27 at 1 54 17 PM" src="https://user-images.githubusercontent.com/44941782/139128937-81b3a6b3-9a8e-4c2f-bf2a-6da4c0d3bb8f.png">

*Target users* have domain knowledge.
Below is a workflow to create labeling functions. For this task and dataset, it took 1 day for an expert. It is estimated to take a few days for a non expert.

STEPS:
#### Data Collection and Setting a Target

1. Collect data
Collecting unlabeled data: The first step is to put together a large set of unlabeled examples (at least 20,000). For the anti-semitic tweet classifier, the author downloaded close to 25,000 tweets that mention the word “jew.”
2. Label a small dataset to evaluate the labeling functions.
  - The author used 600. It isn’t a large number but it is a good place to start. It provides 200 examples in each data split (ABSTAIN, POSITIVE, NEGATIVE)
  - Use already labeled examples if you have them. Otherwise, pick 600 examples at random and label them.
  - Labeling tools: Google Sheets, Airtable (app to label on phone). Split the labeling if working in teams.

<img width="368" alt="Screen Shot 2021-10-27 at 2 44 11 PM" src="https://user-images.githubusercontent.com/44941782/139135957-aae0fda6-95bf-49f6-ae2f-c6411c3c6503.png">

3. Set a goal:
  - Is the task complicated? 
  - Is 90% accuracy enough?
  - Do we favor precision or recall?
  - The author set at least 90% precision and 30% recall for this anti-semitic tweet classification task

#### Creating labeling functions

4. Start writing labeling functions that fit with your targets. In this example, Precision is favored. So the following examples are designed to achieve that.
  - **NOTE**: programming labeling functions is a technical task. We probably want an interface that can be used to build rules and regex. **BabbleLabble** (see existing systems) could be very useful as well because it can parse a text rule and convert it to a program.

```
# Set voting values.
ABSTAIN = 0 
POSITIVE = 1 
NEGATIVE = 2

# Detects common conspiracy theories about jews owning the world.
GLOBALISM = r"\b(Soros|Adelson|Rothschild|Khazar)"

def jews_symbols_of_globalism(tweet_text):
    return POSITIVE if re.search(GLOBALISM, tweet_text) else ABSTAIN

# a function that returns positive if the tween has one of the common insults
# Common insults against jews
INSULTS = r"\bjew"
(bitch|shit|crow|fuck|rat|cockroach|ass|bast(a|e)rd)"

def insults(tweet_text):
  return POSITIVE if re.search(INSULTS, tweet_text) else ABSTAIN
  
 # If tweet author is jewish then tweet is likely not anti-semitic
 JEWISH_AUTHOR = r"((\bI am jew)|(\bas a jew)|(\bborn a jew))"
 
def jewish_author(tweet_text):
  return NEGATIVE if re.search(JEWISH_AUTHOR, tweet_text) else ABSTAIN
```

5. Go through the examples in the LF set and identify a new potential LF.

6. Add the new LF to the Label Matrix. Check that its accuracy is at least 50%. If different LFs relate to the same topic or concept, they can be grouped together. 

<img width="712" alt="Screen Shot 2021-10-27 at 3 23 35 PM" src="https://user-images.githubusercontent.com/44941782/139141445-50959d9b-6681-4a61-aa92-b92b7bffac54.png">

Important metrics:  
- *Emp accuracy*: fraction of correct LF predictions. 
  - **Target** at least 50% for all LFs, 75% is even better.
- *Coverage* % of samples for which at least one LF provides a label. The goal is to maximize coverage without sacrificing accuracy. 
  - **Target**: at least one LF voting 1 or 0 for at least 65% of the training set.
  - Coverage may be easier to achieve for a domain expert, but ideas for good LFs will come with experience, eg. by iterating over LFs, by labeling the intial datapoints. **NOTE**: in an interaction it is probably useful to show the user samples before asking them for LFs.

LF metrics:
- Polarity: The set of unique labels this LF outputs (excluding abstains)
- Coverage: The fraction of the dataset the LF labels
- Overlaps: The fraction of the dataset where this LF and at least one other LF label
- Conflicts: The fraction of the dataset where this LF and at least one other LF label and disagree
- Correct: The number of data points this LF labels correctly (if gold labels are provided)
- Incorrect: The number of data points this LF labels incorrectly (if gold labels are provided)
- Empirical Accuracy: The empirical accuracy of this LF (if gold labels are provided)

7. Every once in a while use the baseline Majority Vote model (provided in Snorkel Metal) to label the LF set. Update LFs accordingly to optimize score with the Majority Vote model.

8. Check if the Majority Vote model is good enough
  - If the LFs achieve at least 60% coverage
  - If the Majority Vote model achieves achieves more that 60% precision and 60% recall:
    - Train the Snorkel Label Model
  - If the Majority Vote model isn’t good enough:
    - Fix the LFs
    - or go back to step 5 and repeat

9. Train the Label Model

10. Run the Label Model over the training set. Look at the top 100 tweets for each class.

11. If the Label Model works, compute probablistiic labels for the training set. Now we have a classification task with a noisy dataset.

### [Twitter Sentiment Analysis Dataset](https://www.kaggle.com/jp797498e/twitter-entity-sentiment-analysis)

#### Overview
This is an entity-level sentiment analysis dataset of twitter. Given a message and an entity, the task is to judge the sentiment of the message about the entity. There are three classes in this dataset: Positive, Negative and Neutral. We regard messages that are not relevant to the entity (i.e. Irrelevant) as Neutral.

**For multiclass classification**: [see this blog post](https://towardsdatascience.com/using-snorkel-for-multi-label-annotation-cc2aa217986a)

#### Usage
Please use `twitter_training.csv` as the training set and `twitter_validation.csv` as the validation set. Top 1 classification accuracy is used as the metric.

### [Predict reading level of book given review](https://www.kaggle.com/thomaskonstantin/highly-rated-children-books-and-stories?select=children_stories.Csv)

### 2. IMDB Movie Reviews: Sentiment Analysis

### 3. YouTube Comments: SPAM detection
- **See the [Snorkel SPAM Tutorial](https://www.snorkel.org/use-cases/01-spam-tutorial)**

## [Named Entity Recognition datasets](https://github.com/davidsbatista/NER-datasets)
- **See the [Snorkel information extraction tutorial](https://www.snorkel.org/use-cases/spouse-demo) 

### [CoNNL2003 shared task - Language-Independent Named Entity Recognition](https://aclanthology.org/W03-0419/)

### [WNUT2017 Shared Task on Novel and Emerging Entity Recognition](https://aclanthology.org/W17-4418/)

## Topic Modeling

### [Neurips LDA](https://www.kaggle.com/rowhitswami/nips-papers-1987-2019-updated/tasks?taskId=2960)
