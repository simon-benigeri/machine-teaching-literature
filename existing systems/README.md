# machine-teaching-literature

## Existing Systems
Some notes about existing machine teaching systems. We can inspire ourselves from these or integrate them 

### Snorkel Flow by [Snorkel.ai](https://snorkel.ai/platform/#how-it-works)

Existing commercial system based off of SNORKEL.
Snorkel is not quite a machine teaching system, but it can be used to create one. We can define an intereaction where users rapidly annotate data.

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

[Link to GitHub](https://github.com/snorkel-team/snorkel)

The flagship system for data programming with user-provided labeling functions

#### How can we use Snorkel?

Heuristics are called **Labeling Functions (LFs)**. 
Here are some common types of LFs:
- Hard-coded heuristics: usually regular expressions (regexes)
- Syntactics: for instance, Spacy’s dependency trees
- Distant supervision: external knowledge bases
- Noisy manual labels: crowdsourcing
- External models: other models with useful signals

### [BabbleLabble Framework](https://github.com/HazyResearch/babble). 
[paper](https://arxiv.org/pdf/1805.03818.pdf)

**Key**:
**Snorkel Labeling Functions** can be parsed from natural language explanations and this is more efficient interaction.

<img width="492" alt="Screen Shot 2021-10-27 at 2 11 40 PM" src="https://user-images.githubusercontent.com/44941782/139131374-27d586dd-e712-45b6-9e0b-9e8166c8b62b.png">

In BabbleLabble, the user provides a natural language explanation for each labeling decision. 
A semantic parser parses these explanations into labeling functions.
The labeling functions generate noisy labels for an arbitrary amount of unlabeled data, which is used to train a classifier. 
Using explanations seems to provide (5-100 times) faster interaction than using labels.
Labeling functions are imperfect so using a simple rule-based semantic parser works fine.

### [Snorkel Metal](https://github.com/HazyResearch/metal)

Extends Snorkel to multi-task learning settings and includes a data programming formulation with better scaling properties.
Now intergrated into Snorkel. 
The idea is that Multi Task Learning helps learn better representations. 
Learning labeling functions can be seen as learning many small tasks. Below are two introductions and tutorials to understand the concepts.

### [Reef](https://github.com/HazyResearch/reef)
Automatically generates labeling functions from a small labeled dataset

Based off the [Snuba](https://www.paroma.xyz/tech_report_reef.pdf) paper

### [Coral](https://arxiv.org/abs/1709.02477)
Improves the label aggregation process by inferring generative model structure via static analysis of labeling functions

### Resources and tutorials
- [Basics Tutorial for Snorkel MeTaL](https://github.com/HazyResearch/metal/blob/master/tutorials/Basics.ipynb)
- [Tradeoffs of different labeling approaches, like Data Programming or Majority Vote, Explanations or Traditional Labels, Including LFs as features](https://github.com/HazyResearch/babble/blob/master/tutorial/Tutorial3_Tradeoffs.ipynb).

## Alternatives to SNORKEL

### [SKWEAK](https://github.com/NorskRegnesentral/skweak)
Open source python toolkit to programmatically label text, like with Snorkel. Built on top of SpaCy.

<img width="465" alt="Screen Shot 2021-10-27 at 2 07 21 PM" src="https://user-images.githubusercontent.com/44941782/139130800-b970537f-9170-4ca3-9066-77aa0c1033d9.png">

Workflow:
- Start: First, you need raw (unlabelled) data from your text domain. skweak is build on top of SpaCy, and operates with Spacy Doc objects, so you first need to convert your documents to Doc objects using SpaCy.
- Step 1: Then, we need to define a range of labelling functions that will take those documents and annotate spans with labels. Those labelling functions can comes from **heuristics**, **gazetteers**, **machine learning models**, etc. See the [documentation](https://github.com/NorskRegnesentral/skweak/wiki) for more details.
- Step 2: Once the labelling functions have been applied to your corpus, you need to aggregate their results in order to obtain a single annotation layer (instead of the multiple, possibly conflicting annotations from the labelling functions). This is done in skweak using a generative model that automatically estimates the relative accuracy and possible confusions of each labelling function.
- 3: Finally, based on those aggregated labels, we can train our final model. Step 2 gives us a labelled corpus that (probabilistically) aggregates the outputs of all labelling functions, and you can use this labelled data to estimate any kind of machine learning model. You are free to use whichever model/framework you prefer.

# LIST OF PAPERS
## NOTE TO ANDREW AND ANDONG: CHECK OUT ALGORITHMS AND SYSTEMS.
Some papers here look into the **interaction**. For instance, if we start with word embeddings, we can reach a good model faster. With active learning, we can ask the user to annotate important samples.


https://github.com/JieyuZ2/Awesome-Weak-Supervision

Some examples:
- [INTERACTIVE WEAK SUPERVISION: LEARNING USEFUL HEURISTICS FOR DATA LABELING](https://github.com/benbo/interactive-weak-supervision) 
The goal of this approach is help experts discover good labeling functions (LFs). Need to read the paper, but aware that some heuristics are provided.

<img width="848" alt="Screen Shot 2021-10-27 at 3 08 47 PM" src="https://user-images.githubusercontent.com/44941782/139139349-95e20601-2b4b-4538-a770-6f3bf4224c36.png">

- [ACTIVE WEASUL: IMPROVING WEAK SUPERVISION WITH ACTIVE LEARNING](https://github.com/SamanthaBiegel/ActiveWeaSuL)

<img width="902" alt="Screen Shot 2021-10-27 at 3 11 29 PM" src="https://user-images.githubusercontent.com/44941782/139139774-76b9d891-d80c-4053-8db5-5378d175f3b5.png">

- [Ruler: Data Programming by Demonstration for Document Labeling](https://aclanthology.org/2020.findings-emnlp.181/)
Data programming aims to reduce the cost of curating training data by encoding domain knowledge as labeling functions over source data. As such it not only requires domain expertise but also programming experience, a skill that many subject matter experts lack. Additionally, generating functions by enumerating rules is not only time consuming but also inherently difficult, even for people with programming experience. In this paper we introduce Ruler, an interactive system that synthesizes labeling rules using span-level interactive demonstrations over document examples. Ruler is a first-of-a-kind implementation of data programming by demonstration (DPBD). This new framework aims to relieve users from the burden of writing labeling functions, enabling them to focus on higher-level semantic analysis, such as identifying relevant signals for the labeling task. We compare Ruler with conventional data programming through a user study conducted with 10 data scientists who were asked to create labeling functions for sentiment and spam classification tasks. Results show Ruler is easier to learn and to use, and that it offers higher overall user-satisfaction while providing model performances comparable to those achieved by conventional data programming.
