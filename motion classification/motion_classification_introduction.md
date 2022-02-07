# 🚀 Motion Classifier Tutorial: Data Labeling with Snorkel

In this tutorial, we will walk through the process of using Snorkel to build a training set for classifying court docket entries as MOTION or NOT MOTION.

Resources:
* For an overview of Snorkel, visit [snorkel.org](https://snorkel.org)
* You can also check out the [Snorkel API documentation](https://snorkel.readthedocs.io/)
* For some real-world applications, check out [Snorkel Applications](https://www.snorkel.org/resources/)
* Why does this work? See [Data Programming: Creating Large Training Sets, Quickly](https://arxiv.org/abs/1605.07723)
* Snorkel paper: [Snorkel: Rapid Training Data Creation with Weak Supervision](https://arxiv.org/abs/1711.10160)

The goal of this tutorial is to illustrate some basic components and concepts of Snorkel in a simple way, but also to dive into a process of iteratively developing a text classifier in Snorkel.

**The goal of this research is to design an interaction for a non-technical, domain expert to quickly label a dataset.**

To achieve this goal, we start with a basic task: *binary text classification* of court docket entries as MOTION or NOT MOTION.

We have access to a large amount of *unlabeled data* (about 1 300 000 samples) in the form of court docket entries with some metadata. We also have access to about *7000 labeled samples*.

In order to train a classifier, we need to label our data, but doing so by hand for real world applications can often be prohibitively slow and expensive.

In these cases, we can turn to a _weak supervision_ approach, using **_labeling functions (LFs)_** in Snorkel: noisy, programmatic rules and heuristics that assign labels to unlabeled training data.

We'll dive into the Snorkel API and how we write labeling functions later in this tutorial, but as an example, we can write an LF that labels data points with `"MOTION to"` in the docket entry text as MOTION since many motions contain `"MOTION to"`:

```python
from snorkel.labeling import labeling_function

@labeling_function()
def lf_contains_motion_to(x):
    # Return a label of MOTION if "MOTION to" in document text, otherwise ABSTAIN
    return MOTION if "motion to" in x.text.lower() else ABSTAIN
```

The tutorial is divided into four parts:
1. **Loading Data**: We load a US courts docket entries dataset, originally used in ["From data to information: automating data science to explore the U.S. court system"](https://dl.acm.org/doi/abs/10.1145/3462757.3466100).

2. **Writing Labeling Functions**: We write Python programs that take as input a data point and assign labels (or abstain) using heuristics, pattern matching, and third-party models.

3. **Combining Labeling Function Outputs with the Label Model**: We model the outputs of the labeling functions over the training set using a Snorkel's, theoretically-grounded modeling approach, ["Data Programming:
Creating Large Training Sets, Quickly"](https://arxiv.org/abs/1605.07723), which estimates the accuracies and correlations of the labeling functions using only their agreements and disagreements, and then uses this to reweight and combine their outputs, which we then use as _probabilistic_ training labels.

4. **Training a Classifier**: We train a classifier that can predict labels for *any* court docket entry (not just the ones labeled by the labeling functions) using the probabilistic training labels from step 3.

In future work, we'll consider *multiclass text classification* of court docket entries as MOTION type. Multiclass text classication is an important problem to work on because we need to define a process that is robust to *concept drift*. The set of classes could expand or change over time, and we do not want to start the labeling process from scratch.

**Note that this process requires programming, but out target user is not technical.**

If we are successful in these text classification tasks, we will consider  solutions to help non-technical workers label the data without programming themselves. Solutions include:
1. Function building interfaces, as seen on Snorkel Flow.
2. Distant supervision: leveraging external knowledge bases. 
3. Mapping natural language inputs to labeling functions. We can use the [BabbleLabbleFramework](https://github.com/HazyResearch/babble) to parse Snorkel Labeling Functions

![BabbleLabble.png](images/BabbleLabble.png)

4. Interfaces/systems where users can provide annotations, which are then converted to labeling functions. An example of such a technology is [Ruler: Data Programming by Demonstration for Document Labeling](https://aclanthology.org/2020.findings-emnlp.181/)

![Ruler - Labeling Interaction](images/Ruler__Labeling_Interaction.png)

We are also interested in optimizations of the interaction between the user and the system. An example is given by [Ruler: Data Programming by Demonstration for Document Labeling](https://aclanthology.org/2020.findings-emnlp.181/) below:

![Ruler - Labeling Interaction](images/Ruler__DPDB.png)

Some other important questions, raised by [Mallinar et al. 2019](https://arxiv.org/pdf/1812.06176.pdf):
1. How do we provide guidance to users to create effective labeling functions? From [Mallinar et al. 2019](https://arxiv.org/pdf/1812.06176.pdf), users desire guidance on how to optimize for precision, coverage, and bias between positive/negative examples in creating functions.
2. How do we support data exploration? Users may be domain experts, but that does not mean they are familiar with the corpus.
3. How do we provide fast feedback and progress tracking? Users desire to see how each query or labeling function impacts the results with immediate feedback. The feedback can help users actively adjust the labeling functions they provided. Systems that require training on many classes stress the need to know when it's time to move on to a diferent class.
4. How do we support evolving classes? (A framework like Snorkel can do this.)

Other questions:
1. How do we minimize the number of samples the user has to see or label?
2. Can we use active learning, uncertainty sampling, or other techniques to surface *valuable examples*? [Active WeaSuL: Improving Weak Supervision with Active Learning](https://github.com/SamanthaBiegel/ActiveWeaSuL) provides some ideas on this.
3. Can a system learn or define heuristics for data labeling? For instance in [Interactive Weak Supervision: Learning Useful Heuristics for Data Labeling](https://github.com/benbo/interactive-weak-supervision)

![Interactive_weak_supervision](images/Interactive_weak_supervision.png)

Note: For 3. how do we come up with the LF function family? Can it come from [Reef](https://github.com/HazyResearch/reef)? 
