# Data Programming Systems - Snorkel

Here we focus on Snorkel because it's been around for a while and there's a lot to say about it. For alternatives to Snorkel please check out the [Snorkel Alternatives page](https://github.com/simon-benigeri/machine-teaching-literature/blob/main/machine%20teaching%20systems/data%20programming/snorkel_alternatives.md)
## [Snorkel](https://www.snorkel.org/)

[Link to GitHub](https://github.com/snorkel-team/snorkel)

The flagship system for data programming with user-provided labeling functions

### How can we use Snorkel?

Resources:
* For an overview of Snorkel, visit [snorkel.org](https://snorkel.org)
* You can also check out the [Snorkel API documentation](https://snorkel.readthedocs.io/)
* For some real-world applications, check out [Snorkel Applications](https://www.snorkel.org/resources/)
* Why does this work? See [Data Programming: Creating Large Training Sets, Quickly](https://arxiv.org/abs/1605.07723)
* Snorkel paper: [Snorkel: Rapid Training Data Creation with Weak Supervision](https://arxiv.org/abs/1711.10160)

Heuristics are called **Labeling Functions (LFs)**. 
Here are some common types of LFs:
- Hard-coded heuristics: usually regular expressions (regexes)
- Syntactics: for instance, Spacy’s dependency trees
- Distant supervision: external knowledge bases
- Noisy manual labels: crowdsourcing
- External models: other models with useful signals

### Some Snorkel Tutorials
- **See the [Snorkel SPAM Tutorial](https://www.snorkel.org/use-cases/01-spam-tutorial)**
- **See the [Snorkel information extraction tutorial](https://www.snorkel.org/use-cases/spouse-demo)**

## Snorkel Flow by [Snorkel.ai](https://snorkel.ai/platform/#how-it-works)

Existing commercial system based off of Snorkel. Snorkel is not quite a machine teaching system, but it can be used to create one. We can define an intereaction where users rapidly annotate data.
It costs a lot of money, and the challenge here is not to reproduce this platform, but to take ideas from it.

### Key functionality: Programmatically labeling data + UI
1. Users can programmatically label data using labeling function-rules, heuristics, and other custom complex operators
2. Interface to create labeling functions is a push-button UI or Python SDK with integrated notebooks
3. System provides ready-made labeling functions (LF) builders, data exploration tools, and auto-suggest features 
4. Users receive instant feedback with coverage and accuracy estimates of LFs to develop so as to build a high-quality training data set
5. Lots of research that suggests ideas for building a similar system

### Key functionality: Supporting Labeling Function Creation
1. Users can programmatically label data using labeling function-rules, heuristics, and other custom complex operators
2. Interface to create labeling functions is a push-button UI or Python SDK with integrated notebooks
3. System provides ready-made labeling functions (LF) builders, data exploration tools, and auto-suggest features 
4. Users receive instant feedback with coverage and accuracy estimates of LFs to develop so as to build a high-quality training data set

## Extensions to Snorkel

Some extensions to Snorkel can help us lower the technical barrier to creating labeling functions.

### [BabbleLabble Framework](https://github.com/HazyResearch/babble). 
[paper](https://arxiv.org/pdf/1805.03818.pdf)

**Key functionality**:
Snorkel labeling functions can be parsed from natural language explanations.

<img width="492" alt="Screen Shot 2021-10-27 at 2 11 40 PM" src="https://user-images.githubusercontent.com/44941782/139131374-27d586dd-e712-45b6-9e0b-9e8166c8b62b.png">

1. The user provides a natural language explanation for each labeling decision. 
2. A semantic parser parses these explanations into labeling functions.
3. The labeling functions generate noisy labels for an arbitrary amount of unlabeled data, which is used to train a classifier. 

Using explanations seems to provide (5-100 times) faster interaction than using labels. Labeling functions are imperfect so using a simple rule-based semantic parser works fine.

### [Snorkel Metal](https://github.com/HazyResearch/metal)

1. Extends Snorkel to multi-task learning settings and includes a data programming formulation with better scaling properties.
2. Now intergrated into Snorkel. 

The idea is that Multi Task Learning helps learn better representations. Learning labeling functions can be seen as learning many small tasks. Below are two introductions and tutorials to understand the concepts.

#### Resources and tutorials
  - [Basics Tutorial for Snorkel MeTaL](https://github.com/HazyResearch/metal/blob/master/tutorials/Basics.ipynb)
  - [Tradeoffs of different labeling approaches, like Data Programming or Majority Vote, Explanations or Traditional Labels, Including LFs as features](https://github.com/HazyResearch/babble/blob/master/tutorial/Tutorial3_Tradeoffs.ipynb).

### [Reef](https://github.com/HazyResearch/reef)

Reef looks into automatically generating labeling functions from a small labeled dataset. The library is based off the [Snuba](https://www.paroma.xyz/tech_report_reef.pdf) paper

### [Coral](https://arxiv.org/abs/1709.02477)
Improves the label aggregation process by inferring generative model structure via static analysis of labeling functions. Some of the benefits of this research will be integrated into snorkel and snorkel metal, some of it will probably only be available in Snorkel Flow.
