# machine-teaching-literature

This repo organizes my notes on machine teaching related papers.

## [Introduction to Machine Teaching](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/introduction%20to%20machine%20teaching)

You will find an overview of the field, including:
- useful definitions
- links and summaries of some key papers

## [Machine Teaching Systems](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/machine%20teaching%20systems)

This directory is divided into 2 parts.

### 1. [Existing Systems](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/machine%20teaching%20systems/existing%20systems)

You will find links, papers, paper summaries, and descriptions for some existing machine teaching sytems. 

### 2. [Data Programming]((https://github.com/simon-benigeri/machine-teaching-literature/tree/main/machine%20teaching%20systems/data%programming))

Data programming is not machine teaching, but we can use data programming and weak supervision functionalities provided by libraries like Snorkel to build a machine teaching prototype.

This section introduces Snorkel, data programming, weak supervision, extensions to Snorkel, and alternatives to Snorkel.

## [Need to read](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/need%20to%20read)

A folder with papers that seem worth reading but that I have not really looked at.

## [Motion Classification](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/motion%20classification)

The repo in which you'll find the work done with Snorkel on classification of Motions in court docket entries.

### [Datasets](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/motion%20classification/datasets)

This is where I stored the court docket entries data.

There is also a directory in which I listed use cases for a system built with Snorkel. It contains:
  - a description of the process for training a text classifier for antisemtic tweets using Snorkel
    - this process provides:
      - a simple procedure to follow to collect and label data
      - some information on how to define and evaluate labeling functions
      - an example of training the label model and text classifier
  - some links to datasets that can be used for various text processing tasks, like classification and NER
    - Those datasets are probably not very useful because we later focused on court docket entries
