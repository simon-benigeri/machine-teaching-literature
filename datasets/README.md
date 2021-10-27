# Datasets and tasks

## Text Classification

### 1. Antisemitic tweets

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

2. Add it to the Label Matrix and check that its accuracy is at least 50%. Try to get the highest
accuracy possible, while keeping a good coverage. We grouped different LFs together if
they relate to the same topic. (See Appendix 7.2, Figure 10.)
3. Every once in a while we use the baseline Majority Vote model (provided in Snorkel Metal)
to label your LF set. We update LFs accordingly to optimize our score with the Majority
Vote model.
4. If the Majority Vote model achieves more that 60% precision and 60% recall, we train our
Snorkel Label Model. Otherwise, we go back to step 1.
5. To validate the Label Model, we looked at the top 100 most anti-semitic tweets from our
Training set.

### [Twitter Sentiment Analysis Dataset](https://www.kaggle.com/jp797498e/twitter-entity-sentiment-analysis)

#### Overview
This is an entity-level sentiment analysis dataset of twitter. Given a message and an entity, the task is to judge the sentiment of the message about the entity. There are three classes in this dataset: Positive, Negative and Neutral. We regard messages that are not relevant to the entity (i.e. Irrelevant) as Neutral.

#### Usage
Please use `twitter_training.csv` as the training set and `twitter_validation.csv` as the validation set. Top 1 classification accuracy is used as the metric.

### [Predict reading level of book given review](https://www.kaggle.com/thomaskonstantin/highly-rated-children-books-and-stories?select=children_stories.Csv)

### 2. IMDB Movie Reviews: Sentiment Analysis

### 3. YouTube Comments: SPAM detection

## [Named Entity Recognition datasets](https://github.com/davidsbatista/NER-datasets)

### [CoNNL2003 shared task - Language-Independent Named Entity Recognition](https://aclanthology.org/W03-0419/)

### [WNUT2017 Shared Task on Novel and Emerging Entity Recognition](https://aclanthology.org/W17-4418/)

## Topic Modeling

### [Neurips LDA](https://www.kaggle.com/rowhitswami/nips-papers-1987-2019-updated/tasks?taskId=2960)
