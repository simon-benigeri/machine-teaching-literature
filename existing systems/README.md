# machine-teaching-literature

## Existing Systems
Some notes about existing machine teaching systems. We can inspire ourselves from these or integrate them 

### Snorkel Flow by [Snorkel.ai](https://snorkel.ai/platform/#how-it-works)

Existing commercial system based off of SNORKEL.

#### Key functionality: Programmatically labeling data + UI
1. Users can programmatically label data using labeling function-rules, heuristics, and other custom complex operators
2. Interface to create labeling functions is a push-button UI or Python SDK with integrated notebooks
3. System provides ready-made labeling functions (LF) builders, data exploration tools,  and auto-suggest features 
4. Users receive instant feedback with coverage and accuracy estimates of LFs to develop so as to build a high-quality training data set
5. Lots of research that suggests ideas for building a similar system

#### Key functionality: Labeling Functions
1. Users can programmatically label data using labeling function-rules, heuristics, and other custom complex operators
2. Interface to create labeling functions is a push-button UI or Python SDK with integrated notebooks
3. System provides ready-made labeling functions (LF) builders, data exploration tools,  and auto-suggest features 
4. Users receive instant feedback with coverage and accuracy estimates of LFs to develop so as to build a high-quality training data set

## Building blocks we can use

### [Snorkel](https://www.snorkel.org/)

The flagship system for data programming with user-provided labeling functions

#### How can we use Snorkel?

Heuristics are called **Labeling Functions (LFs)**. 
Here are some common types of LFs:
- Hard-coded heuristics: usually regular expressions (regexes)
- Syntactics: for instance, Spacy’s dependency trees
- Distant supervision: external knowledge bases
- Noisy manual labels: crowdsourcing
- External models: other models with useful signals

#### [BabbleLabble Framework](https://github.com/HazyResearch/babble). 
[paper](https://arxiv.org/pdf/1805.03818.pdf)

**Key**:
**Snorkel Labeling Functions** can be parsed from natural language explanations and this is more efficient interaction.

<img width="492" alt="Screen Shot 2021-10-27 at 2 11 40 PM" src="https://user-images.githubusercontent.com/44941782/139131374-27d586dd-e712-45b6-9e0b-9e8166c8b62b.png">

In BabbleLabble, the user provides a natural language explanation for each labeling decision. 
A semantic parser parses these explanations into labeling functions.
The labeling functions generate noisy labels for an arbitrary amount of unlabeled data, which is used to train a classifier. 
Using explanations seems to provide (5-100 times) faster interaction than using labels.
Labeling functions are imperfect so using a simple rule-based semantic parser works fine.

#### [Snorkel Metal](https://github.com/HazyResearch/metal)

Extends Snorkel to multi-task learning settings and includes a data programming formulation with better scaling properties.
Now intergrated into Snorkel. 
The idea is that Multi Task Learning helps learn better representations. 
Learning labeling functions can be seen as learning many small tasks. Below are two introductions and tutorials to understand the concepts.

#### [Reef](https://github.com/HazyResearch/reef)
Automatically generates labeling functions from a small labeled dataset

Based off the [Snuba](https://www.paroma.xyz/tech_report_reef.pdf) paper

#### [Coral](https://arxiv.org/abs/1709.02477)
Improves the label aggregation process by inferring generative model structure via static analysis of labeling functions

#### Resources and tutorials
- [Basics Tutorial for Snorkel MeTaL](https://github.com/HazyResearch/metal/blob/master/tutorials/Basics.ipynb)
- [Tradeoffs of different labeling approaches, like Data Programming or Majority Vote, Explanations or Traditional Labels, Including LFs as features](https://github.com/HazyResearch/babble/blob/master/tutorial/Tutorial3_Tradeoffs.ipynb).


### [SKWEAK](https://github.com/NorskRegnesentral/skweak)
Open source python toolkit to programmatically label text, like with Snorkel. Built on top of SpaCy.

<img width="465" alt="Screen Shot 2021-10-27 at 2 07 21 PM" src="https://user-images.githubusercontent.com/44941782/139130800-b970537f-9170-4ca3-9066-77aa0c1033d9.png">

Workflow:
- Start: First, you need raw (unlabelled) data from your text domain. skweak is build on top of SpaCy, and operates with Spacy Doc objects, so you first need to convert your documents to Doc objects using SpaCy.
- Step 1: Then, we need to define a range of labelling functions that will take those documents and annotate spans with labels. Those labelling functions can comes from **heuristics**, **gazetteers**, **machine learning models**, etc. See the [documentation](https://github.com/NorskRegnesentral/skweak/wiki) for more details.
- Step 2: Once the labelling functions have been applied to your corpus, you need to aggregate their results in order to obtain a single annotation layer (instead of the multiple, possibly conflicting annotations from the labelling functions). This is done in skweak using a generative model that automatically estimates the relative accuracy and possible confusions of each labelling function.
- 3: Finally, based on those aggregated labels, we can train our final model. Step 2 gives us a labelled corpus that (probabilistically) aggregates the outputs of all labelling functions, and you can use this labelled data to estimate any kind of machine learning model. You are free to use whichever model/framework you prefer.

# LIST OF STUFF
https://pythonrepo.com/repo/JieyuZ2-Awesome-Weak-Supervision-python-deep-learning

