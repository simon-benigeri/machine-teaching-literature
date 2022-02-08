
# Existing Machine Teaching Systems
Some notes about existing machine teaching systems. We can inspire ourselves from these to think about building out own.

## [Microsoft - LUIS (Language Understanding)](https://www.luis.ai/)
- Part of the Azure stack. Integrates NLU capabilities into chatbots, apps, and IOT devices.
- Provides language models for intent classification and entity extraction.
  - Users can create app, bot, or device specific dictionaries. These are leveraged by the language models.
- Uses active learning to help with continuous improvement.

## [Microsoft - Project Bonsai](https://docs.microsoft.com/en-us/bonsai/product/)
- Part of the Azure stack. Creates autonomous systems for industrial applications.
- A machine teaching platform that leverages:
  - Instructions from engineers (domain expertise)
  - Simulation (for training)
  - Deep reinforcement learning (for optimal control)
- Some more links:
  - [Autonomous Systems - Project Bonsai - How it Works](https://www.microsoft.com/en-us/ai/autonomous-systems-project-bonsai-how-it-works)
  - [Azure - Project Bonsai](https://azure.microsoft.com/en-us/services/project-bonsai)

## [Microsoft - Conversation Learner – A Machine Teaching Tool for Building Dialog Managers for Task-Oriented Dialog Systems (Shukla, Liden, et al., 2020)](https://arxiv.org/abs/2004.04305)
The industry standard in task-oriented dialog systems help dialog authors define rule-based dialog managers, representing dialog flows. These are interpretable and good for simple scenarios but are too brittle/lack flexibility for complex dialogs.

Typical task oriented dialog system architecture:

![](images/conversation_learner__dialog_system_architecture.png)

Machine-learning based approaches are more flexible, but are not interpretable and require lots of training data.

This paper introduces **Conversation Learner**. It is a machine teaching tool for building dialog managers. It combines the best of both approaches.
  - Dialog authors can create a dialog flow using familiar tools.
  - The dialog flow is converted into a parametric model (e.g., neural networks).
  - Dialog authors can improve the dialog manager (i.e., the parametric model) over time by leveraging user-system dialog logs as training data through a machine teaching interface.

The architecture of Conversation Learner (Top) and the development of DMs using Conversation Learner (Bottom):

![](images/conversation_learner__architecture.png)

## [Intel - Semi-supervised Interactive Intent Labeling (Sahai et al., 2021)](https://arxiv.org/abs/2104.13406)

This paper presents a system to speed up training for intent classification in dialog systems. Developers can in interactively label and augment training data from unlabeled utterance corpora using advanced clustering and visual labeling methods. Some of the interesting ideas are:
  - word embeddings and sentence embeddings (SBERT) for semantic similarity and clustering
  - data augmentation techniques like oversampling to improve clustering
  - an interaction to explore and label data that leverages the feedback that these technologies can provide

![](images/SSILS_interactive_labeling_system.png)

## [Machine Teaching for Inverse Reinforcement Learning: Algorithms and Applications (Brown et al., 2018)](https://arxiv.org/abs/1805.07687)

This paper shows how Machine Teaching can make for more effcicient inverse reinforcement learning systems.

Inverse reinforcement learning (IRL) infers a reward function from demonstrations. Given this reward function, an agent learns a policy (a distribution of actions over states) that maximizes cumulative expected rewards. In other words, the agent learns a sequential decision making task.

Machin Teaching can help achieve the minimum set of demonstrations needed to teach a specific sequential decision-making task. The paper covers ideas like "maximally informative demonstrations."

## [Interaction Design for Machine Teaching to Develop AI Tutors (Weitekamp III et al., 2020](https://dl.acm.org/doi/abs/10.1145/3313831.3376226)

Watch this [video](https://www.youtube.com/watch?v=S9Gp2j7I5mU). It's only 30 seconds long.

## [Cambridge Semantics, Parabole.ai - Using Machine Teaching in Text Analysis](https://usc-isi-i2.github.io/KDD2020workshop/papers/KGE1_paper_10.pdf)

This paper is a case study on using Machine Teaching with knowledge graphs. It lacks detail and is pretty shots. I also wonder if they put "teaching" instead of "learning." But the paper makes the case that it is useful to leverage knowledge graphs in combination with key words, phrases, and concepts provided by subject matter experts.

# Data Programming and Weak Supervision
The following section introduces Data Programming and Weak Supervision. The goal is to show technologies that can be used to design a machine teaching system.

## TODO:
1. Put intro to snorkel here. Include description of data programming, weak supervision, and training on noisy labels.
2. Explain why Data Programming is a good idea
  - MT as finding a training set.
    - the optimal training set has minimum cost and generalization error
      - we can reduce the cost not only by intelligently exploring samples (by informativeness and difficulty) but by defining functions to programmatically label the data
        - Data Programming is FAST. We can find an interaction through which the user iteratively explores data and creates/edits labeling functions until the labeling functions sufficiently cover the dataset. Then the system can aggregate these functions and train a model.
      - we can use data science skills (balancing the dataset, data augmentation, cross validation, hyperparameter tuning, model selection, etc.) to help with generalization error
  - MT as infusing domain expertise or concepts.
    - users can define labeling functions to teach concepts.
      - using keywords, regex, distant supervision, etc...
    - we need to have one interface for users to communicate concepts in such a way that the system can parse them into labeling functions. Given a set of labeling functions, the system can evaluates them, aggregates them, etc.
      - can we map some of the design techniques in Knowledge Decomposition paper to types of labeling functions?
      - given types of labeling functions, can we write code to make this function technically accessible?
        - eg. User is prompted "Give me a keyword and the corresponding label". Machine uses tuple (keyword, label) to create a labeling function.
3. Include all major links to snorkel papers and tutorials here.
4. Cleanup the notes below so that they can find their way around Snorkel related libraries.

### Snorkel Flow by [Snorkel.ai](https://snorkel.ai/platform/#how-it-works)

Existing commercial system based off of Snorkel.
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

### Expanding Snorkel

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

##### Resources and tutorials
  - [Basics Tutorial for Snorkel MeTaL](https://github.com/HazyResearch/metal/blob/master/tutorials/Basics.ipynb)
  - [Tradeoffs of different labeling approaches, like Data Programming or Majority Vote, Explanations or Traditional Labels, Including LFs as features](https://github.com/HazyResearch/babble/blob/master/tutorial/Tutorial3_Tradeoffs.ipynb).

#### [Reef](https://github.com/HazyResearch/reef)
  - Automatically generates labeling functions from a small labeled dataset
  - Based off the [Snuba](https://www.paroma.xyz/tech_report_reef.pdf) paper

#### [Coral](https://arxiv.org/abs/1709.02477)
- Improves the label aggregation process by inferring generative model structure via static analysis of labeling functions

### Alternatives to Snorkel

#### [SKWEAK](https://github.com/NorskRegnesentral/skweak)
Open source python toolkit to programmatically label text, like with Snorkel. Built on top of SpaCy.

<img width="465" alt="Screen Shot 2021-10-27 at 2 07 21 PM" src="https://user-images.githubusercontent.com/44941782/139130800-b970537f-9170-4ca3-9066-77aa0c1033d9.png">

Workflow:
- Start: First, you need raw (unlabelled) data from your text domain. skweak is build on top of SpaCy, and operates with Spacy Doc objects, so you first need to convert your documents to Doc objects using SpaCy.
- Step 1: Then, we need to define a range of labelling functions that will take those documents and annotate spans with labels. Those labelling functions can comes from **heuristics**, **gazetteers**, **machine learning models**, etc. See the [documentation](https://github.com/NorskRegnesentral/skweak/wiki) for more details.
- Step 2: Once the labelling functions have been applied to your corpus, you need to aggregate their results in order to obtain a single annotation layer (instead of the multiple, possibly conflicting annotations from the labelling functions). This is done in skweak using a generative model that automatically estimates the relative accuracy and possible confusions of each labelling function.
- Step 3: Finally, based on those aggregated labels, we can train our final model. Step 2 gives us a labelled corpus that (probabilistically) aggregates the outputs of all labelling functions, and you can use this labeled data to estimate any kind of machine learning model. You are free to use whichever model/framework you prefer.

### Improving the Data Programming Interaction:
Some papers in the [Awesome Weak Supervision](https://github.com/JieyuZ2/Awesome-Weak-Supervision) repo look into the **interaction** aspect of Data Programming based approaches.

Some examples that caught my eye:
#### [INTERACTIVE WEAK SUPERVISION: LEARNING USEFUL HEURISTICS FOR DATA LABELING](https://github.com/benbo/interactive-weak-supervision) 
The goal of this approach is help experts discover good labeling functions (LFs). Need to read the paper, but aware that some heuristics are provided.

<img width="848" alt="Screen Shot 2021-10-27 at 3 08 47 PM" src="https://user-images.githubusercontent.com/44941782/139139349-95e20601-2b4b-4538-a770-6f3bf4224c36.png">

#### [ACTIVE WEASUL: IMPROVING WEAK SUPERVISION WITH ACTIVE LEARNING](https://github.com/SamanthaBiegel/ActiveWeaSuL)

<img width="902" alt="Screen Shot 2021-10-27 at 3 11 29 PM" src="https://user-images.githubusercontent.com/44941782/139139774-76b9d891-d80c-4053-8db5-5378d175f3b5.png">

#### [Ruler: Data Programming by Demonstration for Document Labeling](https://aclanthology.org/2020.findings-emnlp.181/)
  - Data programming aims to reduce the cost of curating training data by encoding domain knowledge as labeling functions over source data. As such it not only requires domain expertise but also programming experience, a skill that many subject matter experts lack. Additionally, generating functions by enumerating rules is not only time consuming but also inherently difficult, even for people with programming experience. In this paper we introduce Ruler, an interactive system that synthesizes labeling rules using span-level interactive demonstrations over document examples. Ruler is a first-of-a-kind implementation of data programming by demonstration (DPBD). This new framework aims to relieve users from the burden of writing labeling functions, enabling them to focus on higher-level semantic analysis, such as identifying relevant signals for the labeling task. We compare Ruler with conventional data programming through a user study conducted with 10 data scientists who were asked to create labeling functions for sentiment and spam classification tasks. Results show Ruler is easier to learn and to use, and that it offers higher overall user-satisfaction while providing model performances comparable to those achieved by conventional data programming.
