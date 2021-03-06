# machine-teaching-literature

## Introduction to Machine Teaching

### Useful definitions:

**Machine learning** focuses on creating new algorithms and *improving the accuracy of learners*.  

**Machine teaching** focuses on the *efficacy of the teachers given the learners*. It follows and extends principles of software engineering and programming languages. The emphasis is on the teacher, the teacher's interaction with the data, as well as techniques and design principles of interaction and visualization. 

**Curriculum learning** focuses on *improving the accuracy of learners* by presenting examples not randomly, but organized in a meaningful order which illustrates gradually more concepts, and gradually more complex ones. Curriculum learning lies at the intersection of machine learning and machine teaching and we can use it to build a better MT system.([Bengio et al., 2009](https://ronan.collobert.com/pub/matos/2009_curriculum_icml.pdf))
  - The following paper provides a recent overview of curriculum learning. [Curriculum Learning: A Survey (Soviany et al., 2021)](https://arxiv.org/abs/2101.10382)

[**Iterative Machine Teaching (Liu, Dai et al., 2017)**](https://arxiv.org/abs/1705.10470) studies a machine teaching paradigm where the learner uses an iterative algorithm and a teacher can feed examples sequentially and intelligently based on the current performance of the learner. This area of research helps us think about how to account for:
  - how much the teacher knows about the learner
  - difficulty of samples
  - informativeness/usefulness of samples

![](images/iterative_machine_teaching.png)

The paper [**Teaching a black-box learner(Dasgupta et al., 2019)**](http://proceedings.mlr.press/v97/dasgupta19a.html) considers the problem of teaching a learner whose representation and hypothesis class are unknown: that is, the learner is a black box. A teacher who does not interact with the learner can do no better than providing random examples. However, by interacting with the black-box learner, a teacher can efficiently find a set of teaching examples that is a provably good approximation to the optimal set.

**Knowledge decomposition** is the process of identifying and expressing useful knowledge. In Machine Teaching experts incrementally build semantic ML models in efficient ways. The paper [Understanding and Supporting Knowledge Decomposition for Machine Teaching (Ng, Suh, Ramos., 2020)](https://www.microsoft.com/en-us/research/publication/understanding-and-supporting-knowledge-decomposition-for-machine-teaching/) looks at this process for text or document classification.

**Inverse reinforcement learning** and **deep reinforcement learning** have been put forward in some machine teaching papers as a way to optimize the machine teaching process. They are used in systems like **[Microsoft Project Bonsai](https://azure.microsoft.com/en-us/services/project-bonsai/)**. For now we will not explore this. The key idea is that given a teacher's sequential input, we can learn a policy to interpret these inputs so as to maximize the efficacy of the learner.

# Papers and articles

## Paper 1: [Machine Teaching - A New Paradigm for Building Machine Learning Systems (Simard et. al, 2017)](https://arxiv.org/abs/1707.06742)

Machine Teaching introduces a way to decouple knowledge about machine learning algorithms from the process of teaching.   

### The Machine Learning Lifecycle

**Machine learning** focuses on creating new algorithms and *improving the accuracy of learners*.  

#### Challenges of the Machine Learning lifecycle
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

### Machine Teaching

**Machine teaching** focuses on the *efficacy of the teachers given the learners*. 

The metrics of machine teaching measure performance relative to human costs:
- productivity
- interpretability
- robustness
- scaling with the complexity of the problem
- scaling with the number of contributors

Source for following summary: [Francisco Bernardo summary of machine teaching paper](https://franciscobernardo.medium.com/simard-et-al-machine-teaching-a-new-paradigm-for-building-machine-learning-systems-review-b596bca290c4)

#### Decoupling machine learning from machine teaching

The emphasis is on the teacher, the teacher's interaction with the data, as well as techniques and design principles of interaction and visualization. 

Under the MT paradigm, the teacher is shielded from training and optimizing a machine learning solution. The MT solution uses well-defined and standardised interfaces and ML algorithms that support those interfaces. 

These interfaces should:
1. describe inputs (feature values) and outputs (labels, predictions) of learning algorithms
2. enable ???examples to be distinguished in meaningful ways???
3. enable the addition and removal of features for improving feature blindness and approximation error, and 
4. enable the addition of labelled examples to to improve the estimation error.

MT follows and extends principles of software engineering and programming languages such as
- modularisation and decomposition to solve complex problems
- supporting collaboration through adoption of standardised tools (e.g., programming languages, APIs, documentation, design patterns, componentisation, version control, etc.). This enables to scale to multiple contributions to the solution of the complex problem. 

#### The role of machine teachers according to Simard et al.

???The role of the teacher is to transfer knowledge to the learning machine so that it can generate a useful model that can approximate a concept???. They provide the following set of operational definitions for understanding what they meant:
- A concept is a mapping from any example to a label value.
- A feature is a concept that assigns each example a scalar value.
- A teacher is the person who transfers concept knowledge to a learning machine.
- Selection is the process by which teachers gain access to an example that exemplies useful aspects of a concept.
- A label is a (example, concept value) pair created by a teacher in relation to a concept.
- A schema is a relationship graph between concepts.
- A generic feature is a set of related feature functions.
- Decomposition is the act of using simpler concepts to express more complex ones.

![](images/teaching_concepts.png)

#### Principles for machine teaching according to Simard et al.

- Universal Teaching Language
    - To support different teachers, MT systems need a standard language. The authors propose a simple and easy-to-learn interface:
        - that is agnostic of ML algorithms
          - data exploration logic consistent across different algorithms
          - feature and concept definition consistent across different algorithms
        - that enables teachers to exchange them according to the best fit for the concept to learn
          - eg. swapping a BERT model for one trained on a particular domain
          - eg. swapping models and feature selection algorithms for image classification to models used for text classification
          -  classifier for a language model
- Feature completeness 
    - all desired target concepts should be ??? ???realisable??? through a composition of models and features???. 
    - a key assumption in the paper is that it is the system???s responsibility to provide feature completeness
      - so that the teacher can focus on exploring, adding and discriminating features and examples to augment the capacity of the system to model the concept.
- Rich and diverse sampling set 
    - the dataset should enable the teacher to explore it ???to express knowledge through selection???.
    - Simard et al. propose the need for new ways of collecting data that retain as much of the semantic value of data as possible. 
    - They imply that storing data indiscriminately could be a solution (???effort of storing data is negligible compared to the cost of teaching???).
- Distribution robustness 
    - teacher should be able to explore and label freely without concerns
    - Another assumption made is that a teacher will be able reach a correct teaching outcome (i.e., a robust model that is correct for any example) given a rich and diverse sampling set, feature completeness, and ML algorithms that are robust to covariate shift. 
    - Covariate shifts refer to changes in the distribution of the new examples that decrease the efficacy of a deployed model.
      - Covariate shifts are one of causes for models to break and that require a new model-building iteration. 
      - This is definitely a constraint for MT applications and the MT process.
- Modular development 
    - MT should support decomposition in concept modelling through modular development
      - decomposing concepts into sub-concepts, 
      - using models as features of other models
      - The authors think we can achieve this by standardising interfaces for models and features, in analogy to elements of integrated development environments, such as solution, projects and project dependencies.
- Version Control 
    - all teacher???s actions are relevant and contribute to build a concept ???program???. 
    - they should be stored, analog to code versioning and commits, and used to facilitate collaboration between different teachers and integrate their contributions.

#### Example of a Machine Teaching Process

![](images/machine_teaching_process_simard.png)

## Paper 2: [Microsoft Machine Teaching Overview](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/articles/machine-teaching)

Microsoft describes Machine Teaching as a new paradigm for machine learning systems that:
- Combines subject matter expertise from human domain experts with AI and ML.
- uses deep reinforcement learning to identify patterns in the learning process and adopt positive behaviors in its own methods.
- Leverages simulated environments to generate large amounts of synthetic data for domain-specific use cases and scenarios.
- Provides for greater explainability of the behavior of resulting models.

### Comments:
This page provides plenty of information on this view of Machine Teaching. It shows how to leverage technologies like Deep RL, simulation, etc. I did not try to  explore this in any detail. Diving into applications of deep RL and simulation for a prototype that was first described as "maybe we should start by having the user  with couple regex and some keyword search" seemed like using a bazooka to kill a fly. However, I want to draw your attention to the flowcharts and methodologies provided by microsoft. I think they can help you design the application you need to build. Also if you think you can make this Deep RL thing work - go for it.

### Building a Machine Teaching System

#### Machine Teaching Process build and development

The following chart describes the build and development process with 3 stages: build, train, and deploy.

![](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/media/machine-teaching-1-2.png)

**Build Phase**:
- Write the machine teaching program.
- Connect it to a domain-specific training simulator.
    - simulators are supposed to generate sufficient training data for experiments and machine practice. **I'm not really sure how we can simulate training data for a use case like classfying court docket entries.**

**Train Phase**:
- Use a Microsoft training engine to generate and train a deep reinforcement learning model.
  - This requires "high level domain models" with appropriate RL algorithms and neural networks. **I'm not sure what these "high level domaim models" are...maybe you can use the Satyrn domain ontologies.**

**Deploy Phase**:
- Deploys the trained model to the target application in the cloud, on-premises, or embedded on site.

Hopefully now you can see why I did not think this was the right approach for this Capstone.

#### The Machine Learning Process:

![](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/media/machine-teaching-2-3.png)

1. The problem owner collects and labels data.
2. The problem owner reviews quality of labeled data.
3. Machine-learning experts select an algorithm, model architecture, objective function, regularizers, and cross-validation sets.
4. Engineers train the model cyclically, adjusting the features or creating new features to improve model accuracy and speed.
5. The model is tested on a small sample. If the system doesn't do well in the test, the preceding steps are repeated.
6. Model performance is monitored in the field. If performance falls below a critical level, the model is modified by repeating the preceding steps.

Machine teaching automates the creation of such models, easing the need for manual intervention in the learning process to improve feature selection or examples, or tweaking of hyper-parameters. In effect, **machine teaching introduces a level of abstraction into the AI elements of the model, allowing the developer to focus on the domain knowledge.** This abstraction also allows the AI algorithm to be replaced by new more innovative algorithms in time, without requiring a respecification of the problem.

#### The role of the teacher
The role of the teacher is to optimize the transfer of knowledge to the learning algorithm so it can generate a useful model. 
Teachers also play a central role in data collection and labeling. Teachers can:
- filter unlabeled data to select specific examples.
- look at the available example data and guess its label based on their own intuition or biases.
- Similarly, given two features on a large unlabeled set, teachers can conjecture that one is better than the other.

The following image shows the high-level process of machine teaching:

![](https://docs.microsoft.com/en-us/azure/architecture/solution-ideas/media/machine-teaching-2-6.png)

1. The teacher first questions whether a training set is realizable.
2. If the training set isn't realizable, the teacher determines whether the issue is due to inadequate labeling or feature deficiencies. After correcting the labeling or adding features, the teacher again assesses whether the training set is realizable.
3. If the training set is realizable, the teacher assesses whether training quality criteria are being met.
4. If quality criteria aren't being met, the teacher finds the test errors and adds the fixes to the training set, then repeats the assessment steps.
5. Once the training set is realizable and quality criteria are met, the process finishes.

### Key Take Away:
We can use this resource to understand how to build our own Machine Teaching System. 

#### We need to provide teaching capabilities
The role of the teacher is described a bit more concreteley. The teacher:
- explores and labels data
- provides some input to define features or concepts
- judge features and concepts based on their contribution to the machine learning system's performance
- interact with the data and machine learning system until the machine learning system's performance is satisfactory.

**One way to do this is to define an interaction by which a teacher can quickly create a labeled dataset**.

#### We need to provide to handle the machine learning part ourselves
The ML training needs to be abstracted away from the user. It does not have to use complicated algorithms. For example, given a 

## Papers 3 and 4: [Machine Teaching - An Inverse Problem to Machine Learning and an Approach Toward Optimal Education (Zhu, 2015)](https://www.semanticscholar.org/paper/Machine-Teaching%3A-An-Inverse-Problem-to-Machine-and-Zhu/f83ca18f3834d45a70e9b54578e2c33870dde67d) and [An Overview of Machine Teaching (Zhu et al., 2018)](https://arxiv.org/abs/1801.05927)

These two papers are described together because they come from the same author and the takeaways we need for our problem are the same in both papers.

### Machine Teaching Definition

Machine Teaching is the process of finding an optimal training set given a learner. 

We can view a machine learning algorithm *A* as a function that maps the space of training sets **D** to a model space **&theta;**:

![](images/MT_optimal_training_set.png)

Let's say we have a target *learner* or model *&theta;<sup>*</sup>*. Given a training set *D* in **D**, machine learning returns a model *A(D)* in **&theta;**. This is a many to one relation. Given a target model *&theta;<sup>*</sup>* the inverse function *A<sup>-1</sup>(&theta;*<sup>*</sup>*)* will return the **set of training sets that will result in** *&theta;<sup>*</sup>*.

Machine teaching aims to find the optimal member in *A<sup>-1</sup>(&theta;*<sup>*</sup>*)*. This is the training set with minimal cost, where cost might be:
- the training set size
- generalization error
- etc.

Finding *A<sup>-1</sup>* is difficult. It may not even exist for some target model. This is the problem that machine teaching focuses on.

### What does this mean for us?

Practically speaking, we need to consider:
- **the target model**: a learner that is good enough for the user's problem
- **the optimal dataset** => we can relax this to think about **a good enough dataset**. In other words, a dataset that will yield good enough performance for the user's problem.

#### Reducing the set of possible learners

We can reduce the set of possible learners by mapping use cases or taks to specific models. For example, for a text classification task, the target learner can be chosen by the application builder. We can choose to use an ngram based feature extraction followed by an SVM. Or we can choose to throw the labeled dataset into one of the faster and cheaper pretrained language models (like DistilBERT) with a classification layer.

#### Translating "finding an optimal training set" into something we can do:

Our task is therefore to find an interaction where the user can create a good enough dataset to train a given model. And we want to minimize the cost of creating this dataset.


## Paper 5: [Iterative Machine Teaching (Liu, Dai et al., 2017)](https://arxiv.org/abs/1705.10470)

This paper studies a machine teaching paradigm where the learner uses an iterative algorithm and a teacher can feed examples sequentially and intelligently based on the current performance of the learner.

![](images/iterative_machine_teaching.png)

### Achieving fast convergence in the learner model

Instead of constructing a minimal training set for learners, iterative machine teaching focuses on achieving fast convergence in the
learner model. 

There are different categories of teachers, based on how much information the teacher has from the learner model. For each level of information, the paper proposes an algorithm to achieve fast convergence.

### Key Ideas for us:

1. It is useful to consider teachers as having different levels of information about the models.
2. An iterative teaching process can help achieve fast convergence in the learner model.
    - Can we flip this around and ask? **Can an iterative process help achieve fast creation of a minimal training set?**
3. The teacher and the student (learner) do not need the same representation of a sample of data. They need to be deterministically related though.
    - eg. or text classification applications, the learner can work with pretrained word or sentence embeddings of a sample and the teacher can work with the sample itself.
  - the teacher can work with a labeling function's logic and the student can work with the labeling function itself.

```python
from snorkel.labeling import labeling_function

@labeling_function()
def lf_contains_keyword(x: str, keyword: str, label: str):
    # Return a given label if keyword in sample text
    return label if keyword in x.text.lower() else ""
```
4. Some ways to think about the difficulty of an example: 
    - Given the model's parameters, what is the probability of a wrong label?
    - How much information does an example carry? (similar to curriculum learning)
5. Some ways to thing about the usefulness of an example:
    - the correlation between discrepancy (some distance between teacher and learner) and the information (difficulty) of an example. If the information of the example has large correlation with the discrepancy, it means that this example is very useful in this teaching iteration.
6. There are a few models of a teacher's knowledge about the learner. We did not explore those but these models can help make the right choices in designing an iterative teaching process.

## Paper 6: [Understanding and Supporting Knowledge Decomposition for Machine Teaching (Ng, Suh, Ramos., 2020)](https://www.microsoft.com/en-us/research/publication/understanding-and-supporting-knowledge-decomposition-for-machine-teaching/)

### What is knowledge decomposition?
Knowledge decomposition is the process of identifying and expressing useful knowledge. In Machine Teaching experts incrementally build semantic ML models in efficient ways. This paper seeks to build foundational frameworks for understanding and supporting this process. The authors looked at the task of teaching a learner to classify text documents. They investigated:
  - what types of knowledge do people want to teach?
  - what types of decomposition structures do people use to represent the knowledge they want to teach?
  - what cognitive processes do people use to identify and express the knowledge they want to teach?
  - what challenges do people face during knowledge decomposition?

The paper offers some design ideas for supporting knowledge decomposition in machine teaching and this is beneficial for building systems that help domain experts infuse a learner with concepts.

### Why knowledge decomposition?
Machine Teaching goes beyond labeling data. Human teachers possess and can offer richer forms of knowledge than just labels.
  - eg. a teacher may know about features, concepts, relationships, rules, and other strategies that are useful for recognizing dogs
    - a teacher can select specific examples of images and label them as "Dog" or "Not Dog"
    - a teacher can also provide semantic explanations about why an image is labeled as such
  - this semantic information can make the teaching or labeling process more efficient
    - because there's no need to label samples one by one
    - because the learner can provide semantic information back to the user

### Studying knowledge decomposition in a text classification task

The authors collected news articles on topics like "Food" and "Business" and asked participants to participate in 2 tasks to study knowledge decomposition.

#### Labeling and annotation task

Participants were asked:
  - to find at least 2-3 examples of articles for each of the 2 labels (i.e., "Food", "Business")
    - to annotate which parts of the articles helped them determine how to label them
    - participants were allowed to count a multi-label document as both an example of "Food" and an example of "Business"

#### Knowledge summary task

Participants were asked:
  - to create a summary of all the useful knowledge they thought the machine needs in order to label articles as "Food" and/or "Business"
    - they wrote and/or drew them on Post-it notes and large poster paper
    - participants were allowed to include any knowledge from the articles or from their own memory and to structure their knowledge summary in any way

### Results

#### 1. Types of Knowledge

The authors identified 3 categories of knowledge types that participants thought were useful for the learner to understand in order to perform the multi-label classification task 
  - concepts
  - relationships
  - rules 
  - (as well as sub-categories within each)

**Concepts** are ideas or notions related to the decision to be made. 5 sub-categories of concepts that participants wanted to teach:
  - Semantic concepts
    - these are dependent on label meanings
      - i.e. in the study, the labels were "Food" and "Business"
      - e.g. "types of food," "food actions/verbs," "recipe,", "types of business," "buying/selling," and "money" 
    - for many semantic concepts, participants listed keywords or symbols
      - e.g., keywords like "cookie" and "beef" are indicators of the concept "types of food"
  - Structural concepts
    - these are independent of label meanings, but dependent on components of the data type
      - i.e. in the study, the the data type was text-based news articles)
      - e.g. "title," "sub-headers," "author," "paragraphs," "ordered lists,", "sentences," and "words"
  - Stylistic concepts
    - these depend only on the overall data type
      - i.e. in the study, the overall data type was text
      - e.g. linguistic style concepts such as "language" (i.e., English), "tone," "informality," and "figures of speech,"
      - e.g. visual style concepts such as "font type" and "font size"
  - Meta concepts
    - these are independent of label meanings, independent of data type, and computable as a function of other types of knowledge
      - e.g. implicit meta concepts that require some level of subjective interpretation to determine
        - "main subject", "intended audience," and "goal/intent" of a news article
      - e.g. explicit concepts that can be determined directly based on the article text
        - "presence," "frequency," and "repetition" of keywords or concepts
  - Task goal concepts
    - these are externally- or user-imposed constraints that are not computable from the data itself
      - e.g. "my personal interests/non-interests" such as "real or fake news" and "Thai food"
      - e.g. "my objective" such as speed and accuracy of the ML model

**Relationships**, or schemas, describe relations and constraints between concepts. 2 sub-categories of relationships that participants wanted to teach:
  - Semantic relationships
    - these are based on the meanings of labels and concepts
      - e.g. taxonomical relationships
        - "types of food" is a sub-concept of "food"
        - "company" is an example of "types of business")
      - e.g. positive/negative association
        - "market" is associated with "business"
        - "business" and "politics" are sometimes related
        - "suicide" is rarely related to "food" or "business")
      - e.g. mathematical relationships 
        - word count is greater than five
  - Structural relationships
    - these are independent of label or concept meanings, but dependent on the data type
      - e.g. co-occurrence
        - words/concepts appear together
        - presence of certain words/concepts in the absence of other words or concepts
        - spatial relationships
          - "cookie" is in the title
          - "$" is before a number

**Rules** describe how to apply/combine concepts and relationships to assign labels to documents. 2 subcategories of rules that participants wanted to teach:
 - Procedures
    - these are sequences of steps or if-then statements for how to assign labels to document
      - e.g. instructions on the order in which actions should be performed
        - First look at the title and find these keywords. Next, look at subsection headers. Then look at the body.
      - e.g. criterion that need to be met in order to assign labels
        - "If the frequency of these keywords is greater than 5, then label it as "Food."
 - Weights
   - these are degrees of strength or confidence that the user subjectively assigns to each concept, relationship, procedure, or label
     - e.g. using the words "strong" vs. "weak"
     - e.g. using 1-3 star rating system to indicate the importance each keyword, concept, or relationship to a label
     - e.g. assigning numerical confidence scores to each concept
       - If you see this set of words, then 90% sure it???s this label.
       - If you see this other set of words, then 70% sure it???s this label.
       - If you see this final set of words, then 50% sure it???s this label.

#### 2. Types of Decomposition Structures

The authors observed 3 key dimensions along which the decomposition structures in participants??? knowledge summaries varied:
  - degree of label distinction
  - degree of knowledge type distinction
  - degree of programmable rules

![](images/knowledge_decomposition__Figure3.png)

#### 3. Knowledge Decomposition Processes

The authors observed that participants used an iterative sensemaking process to identify and express the knowledge that they wanted to teach the machine. This process is detailed in the paper and you should check it out.

![](images/knowledge_decomposition__Figure4.png)

#### 4. User Challenges
The authors identified 2 major challenges that participants faced during knowledge decomposition: 

1. Understanding how the learner works
  - e.g. users assumed the learner was a decision tree
2. Articulating abstract and implicit knowledge
  - e.g. "target audience" of an article, or "context"

Other challenges observed:
3. Access to existing lists, dictionaries, and lexicons
4. Flexibility to revise knowledge decomposition
5. Feedback on knowledge usefulness and understandability

### Final Comments:
Please read this paper yourselves! I think it is really helpful in thinking about how to design a Machine Teaching system.
Let's think about the case where we build a system with Snorkel:
  1. We can map the types of concepts to types of labeling functions (see Types of knowledge)
  2. We use define an interaction that supports the iterative sensemaking process described
  3. Labeling functions can access external sources of data (Challenge 3.)
  4. Labeling functions can iteratively be evaluated and edited (Challenges 4. and 5.) 

## Paper 7: [Whither AutoML? Understanding the Role of Automation in Machine Learning Workflows (Xin, Wu, et al., 2021)](https://arxiv.org/abs/2101.04834)

Paper provided by Andrew. Sorry I did not get to a summary.
