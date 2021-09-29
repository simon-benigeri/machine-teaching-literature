# machine-teaching-literature

## Introduction

### Useful definitions:

**Machine learning** focuses on creating new algorithms and *improving the accuracy of learners*.  

**Machine teaching** focuses on the *efficacy of the teachers given the learners*. It follows and extends principles of software engineering and programming languages. The emphasis is on the teacher, the teacher's interaction with the data, as well as techniques and design principles of interaction and visualization. 

**Curriculum learning** focuses on *improving the accuracy of learners* by presenting examples not randomly, but organized in a meaningful order which illustrates gradually more concepts, and gradually more complex ones. Curriculum learning lies at the intersection of machine learning and machine teaching.([Bengio et al., 2009](https://ronan.collobert.com/pub/matos/2009_curriculum_icml.pdf))
- The following paper provides a recent overview of curriculum learning. [Curriculum Learning: A Survey (Soviany et al., 2021)](https://arxiv.org/abs/2101.10382)

**Inverse reinforcement learning** and **Reinforcement learning** have been put forward in some machine teaching papers as a way to optimize the machine teaching process. They are used in systems like **[Microsoft Project Bonsai](https://azure.microsoft.com/en-us/services/project-bonsai/)**. For now we will not explore this.

## Papers

### Microsoft [Machine Teaching Overview](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/machine-teaching)

### [Machine Teaching - A New Paradigm for Building Machine Learning Systems](https://arxiv.org/abs/1707.06742)

#### Summary

Introduces a way to decouple knowledge about machine learning algorithms from the process of teaching.   

**Machine learning** focuses on creating new algorithms and *improving the accuracy of learners*.  

**Machine teaching** focuses on the *efficacy of the teachers given the learners*. It follows and extends principles of software engineering and programming languages. The emphasis is on the teacher, the teacher's interaction with the data, as well as techniques and design principles of interaction and visualization. 

**Curriculum learning** focuses on *improving the accuracy of learners* by presenting examples not randomly, but organized in a meaningful order which illustrates gradually more concepts, and gradually more complex ones. Curriculum learning lies at the intersection of machine learning and machine teaching.([Bengio et al., 2009](https://ronan.collobert.com/pub/matos/2009_curriculum_icml.pdf))
- The following paper provides a recent overview of curriculum learning. [Curriculum Learning: A Survey (Soviany et al., 2021)](https://arxiv.org/abs/2101.10382)

**Inverse reinforcement learning** and **Reinforcement learning** have been put forward in some machine teaching papers as a way to optimize the machine teaching process. They are used in systems like **[Microsoft Project Bonsai](https://azure.microsoft.com/en-us/services/project-bonsai/)**. For now we will not explore this.

#### Key Ideas

**Machine teachining** focuses on the *efficacy of the teachers given the learners*. The metrics of machine teaching measure performance relative to human costs:
- productivity
- interpretability
- robustness
- scaling with the complexity of the problem
- scaling with the number of contributors

**Definition: *Concept evolution***: a process in which the teacher's underlying notion of the target class is defined and refined over time ([Kulesza et al., 2014](https://www.microsoft.com/en-us/research/publication/structured-labeling-for-facilitating-concept-evolution-in-machine-learning/))
- label noise and inconsistencies can arise from concept evolution and negatively affect model performance
- in practice concept definitions, schemas, and labels can change as new sets of rare positives are discovered, or when teachers change their minds
- concept evolution affects productivity because it requires the teacher to relabel examples. From the teacher's perspective
    - concepts should be decomposable into sub-concepts
    - manipulating the relashionship between sub-concepts should be easy, interpretable, and reversible


#### Comments


### Paper Y

