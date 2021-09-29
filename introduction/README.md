# machine-teaching-literature

## Introduction

### Useful definitions:

**Machine learning** focuses on creating new algorithms and *improving the accuracy of learners*.  

**Machine teaching** focuses on the *efficacy of the teachers given the learners*. It follows and extends principles of software engineering and programming languages. The emphasis is on the teacher, the teacher's interaction with the data, as well as techniques and design principles of interaction and visualization. 

**Curriculum learning** focuses on *improving the accuracy of learners* by presenting examples not randomly, but organized in a meaningful order which illustrates gradually more concepts, and gradually more complex ones. Curriculum learning lies at the intersection of machine learning and machine teaching and we can use it to build a better MT system.([Bengio et al., 2009](https://ronan.collobert.com/pub/matos/2009_curriculum_icml.pdf))
- The following paper provides a recent overview of curriculum learning. [Curriculum Learning: A Survey (Soviany et al., 2021)](https://arxiv.org/abs/2101.10382)

[**Iterative Machine Teaching (Liu, Dai et al., 2017)**](https://arxiv.org/abs/1705.10470) studies a machine teaching paradigm where the learner uses an iterative algorithm and a teacher can feed examples sequentially and intelligently based on the current performance of the learner.

<img width="433" alt="Screen Shot 2021-09-29 at 10 08 07 AM" src="https://user-images.githubusercontent.com/44941782/135296788-e3ac02b5-9069-4245-adbd-53de59918699.png">

- [Teaching a black-box learner](http://proceedings.mlr.press/v97/dasgupta19a.html) considers the problem of teaching a learner whose representation and hypothesis class are unknown: that is, the learner is a black box. A teacher who does not interact with the learner can do no better than providing random examples. However, by interacting with the black-box learner, a teacher can efficiently find a set of teaching examples that is a provably good approximation to the optimal set.

**Inverse reinforcement learning** and **Reinforcement learning** have been put forward in some machine teaching papers as a way to optimize the machine teaching process. They are used in systems like **[Microsoft Project Bonsai](https://azure.microsoft.com/en-us/services/project-bonsai/)**. For now we will not explore this.

## Papers

### Microsoft [Machine Teaching Overview](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/machine-teaching)

### [Machine Teaching - A New Paradigm for Building Machine Learning Systems](https://arxiv.org/abs/1707.06742)

#### Summary

Introduces a way to decouple knowledge about machine learning algorithms from the process of teaching.   

**Machine learning** focuses on creating new algorithms and *improving the accuracy of learners*.  

**Machine teaching** focuses on the *efficacy of the teachers given the learners*. It follows and extends principles of software engineering and programming languages. The emphasis is on the teacher, the teacher's interaction with the data, as well as techniques and design principles of interaction and visualization. 

#### Key Ideas

**Machine teaching** focuses on the *efficacy of the teachers given the learners*. The metrics of machine teaching measure performance relative to human costs:
- productivity
- interpretability
- robustness
- scaling with the complexity of the problem
- scaling with the number of contributors
Under the MT paradigm, the teacher is shielded from the complexities of the algorithmic runtime and optimisation procedures with a solution that uses well-defined and standardised interfaces and ML algorithms that support those interfaces. 


**Challenges of the Machine Learning lifecycle**
1. long iterations for model building due to data collection, labelling, training, evaluation, optimisation, etc.
2. maintaining model stability
    - a model can be stable for months until it breaks
    - typically months, until it breaks for many reasons, e.g., covariate shifts, variations in the feature space, label noise, concept evolution, software bugs and updates, etc.)
3. challenges in reproducability and re-iteration due to lack of documentation, lack of available expertise, moving staff, lack of modularity, high maintenance costs, etc.

**Definition: *Concept evolution***: a process in which the teacher's underlying notion of the target class is defined and refined over time ([Kulesza et al., 2014](https://www.microsoft.com/en-us/research/publication/structured-labeling-for-facilitating-concept-evolution-in-machine-learning/))
- label noise and inconsistencies can arise from concept evolution and negatively affect model performance
- in practice concept definitions, schemas, and labels can change as new sets of rare positives are discovered, or when teachers change their minds
- concept evolution affects productivity because it requires the teacher to relabel examples. From the teacher's perspective
    - concepts should be decomposable into sub-concepts
    - manipulating the relashionship between sub-concepts should be easy, interpretable, and reversible


**Decoupling machine learning from machine teaching**
Machine teaching models can require multiple machine learning algorithms throughout the teaching process.
Machine teaching aims to shield the teacher from complexities 

Simard et al. propose MT as an holistic approach to reduce human costs (i.e., required expertise and maintenance time) in the process of teaching a machine learner. Under the MT paradigm, the teacher is shielded from the complexities of the algorithmic runtime and optimisation procedures with a solution that uses well-defined and standardised interfaces and ML algorithms that support those interfaces. These interfaces should 1) describe inputs (feature values) and outputs (labels, predictions) of learning algorithms, 2) enable “examples to be distinguished in meaningful ways”, 3) enable the addition and removal of features for improving feature blindness and approximation error, and 4) enable the addition of labelled examples to to improve the estimation error.

#### Comments


### Paper Y

