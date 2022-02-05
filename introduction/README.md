# machine-teaching-literature

## Introduction to Machine Teaching

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

**Machine teaching** focuses on the *efficacy of the teachers given the learners*. 

The metrics of machine teaching measure performance relative to human costs:
- productivity
- interpretability
- robustness
- scaling with the complexity of the problem
- scaling with the number of contributors

Source for following summary: [Francisco Bernardo summary of machine teaching paper](https://franciscobernardo.medium.com/simard-et-al-machine-teaching-a-new-paradigm-for-building-machine-learning-systems-review-b596bca290c4)

**Decoupling machine learning from machine teaching**
The emphasis is on the teacher, the teacher's interaction with the data, as well as techniques and design principles of interaction and visualization. 

Under the MT paradigm, the teacher is shielded from training and optimizing a machine learning solution. The MT solution uses well-defined and standardised interfaces and ML algorithms that support those interfaces. 

These interfaces should:
1. describe inputs (feature values) and outputs (labels, predictions) of learning algorithms
2. enable “examples to be distinguished in meaningful ways”
3. enable the addition and removal of features for improving feature blindness and approximation error, and 
4. enable the addition of labelled examples to to improve the estimation error.

MT follows and extends principles of software engineering and programming languages such as
- modularisation and decomposition to solve complex problems
- supporting collaboration through adoption of standardised tools (e.g., programming languages, APIs, documentation, design patterns, componentisation, version control, etc.). This enables to scale to multiple contributions to the solution of the complex problem. 

**The role of machine teachers** according to Simard et al.:

“The role of the teacher is to transfer knowledge to the learning machine so that it can generate a useful model that can approximate a concept”. They provide the following set of operational definitions for understanding what they meant:
- A concept is a mapping from any example to a label value.
- A feature is a concept that assigns each example a scalar value.
- A teacher is the person who transfers concept knowledge to a learning machine.
- Selection is the process by which teachers gain access to an example that exemplies useful aspects of a concept.
- A label is a (example, concept value) pair created by a teacher in relation to a concept.
- A schema is a relationship graph between concepts.
- A generic feature is a set of related feature functions.
- Decomposition is the act of using simpler concepts to express more complex ones.

**Principles for MT** according to Simard et al.:

- Universal Teaching Language
    - in order to support and enable different teachers, Simard et al. propose the standardisation of a language as one simple and easy-to-learn interface that is agnostic of ML algorithms, but that provides access to their power by enabling to exchange them according to the best match for the concept to learn.
- Feature completeness 
    - all desired target concepts should be “ ‘realisable’ through a composition of models and features”. The assumption is that it is the system’s responsibility to provide feature completeness, so that the teacher can focus on exploring, adding and discriminating features and examples to augment the capacity of the system to model the concept.
- Rich and diverse sampling set 
    - the data set should enable the teacher to explore it “to express knowledge through selection”. Simard et al. propose the need for new ways of collecting data that retain as much of the semantic value of data as possible. That they imply that storing data indiscriminately could be a solution (“effort of storing data is negligible compared to the cost of teaching”).
- Distribution robustness 
    - teacher should be able to explore and label freely without concerns. A critical assumption made Simard et al. is that a teacher will be able reach a correct teaching outcome (i.e., a robust model that is correct for any example) given a rich and diverse sampling set, feature completeness and ML algorithms that are robust to covariate shift. Covariate shifts refer to changes in the distribution of the new examples that make deployed model or running in the wild, to loose efficacy. It is one of causes for models to break and that require a new model-building iteration. I would say that this is a very difficult conjunction of factors, and should act as a constrain of application of the MT process.
- Modular development 
    - MT should support decomposition in concept modelling through modular development (i.e. decomposing concepts into sub-concepts, using models as features of other models). Simard et. postulate that it can be achieved by standardising interfaces for models and features, in analogy to elements of integrated development environments, such as solution, projects and project dependencies.
- Version Control 
    - all teacher’s actions are relevant and contribute to build a concept “program”. Hence they should be stored, analog to code versioning and commits, and used to facilitate collaboration between different teachers and integrate their contributions.
