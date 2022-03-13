# machine-teaching-literature

This repo organizes my notes on machine teaching related papers. It contains an overview of what I read in the field, a brief description of various machine teaching systems, and an exploration of data programming to build our own machine teaching system.

## [Introduction to Machine Teaching](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/introduction%20to%20machine%20teaching)

This section contains a brief overview of the field. You'll find key definitions as well as links and summaries for some key papers.

### [Need to read](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/introduction%20to%20machine%20teaching/need%20to%20read)

This folder contains papers that I strongly recommend, or that I have not really looked at in enough detail.

## [Machine Teaching Systems](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/machine%20teaching%20systems)

This directory is divided into 2 parts. One part describes existing machine teaching systems. The other introduces data programming, a technology that we can use to build our own.

### 1. [Existing Systems](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/machine%20teaching%20systems/existing%20systems)

This section contains descriptions for some existing machine teaching sytems. There are mostly links and paper summaries.

### 2. [Data Programming](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/machine%20teaching%20systems/data%20programming)

This section introduces Snorkel, data programming, weak supervision, extensions to Snorkel, and alternatives to Snorkel.

## [Motion Classification](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/motion%20classification)

This section contains the code and documentation for classifying Motions in court docket entries with Snorkel.

### [Data](https://github.com/simon-benigeri/machine-teaching-literature/tree/main/motion%20classification/data)

This is section is where I downloaded and accessed the court docket entries data in the code. The data is not published in the repo.

This section also contains a directory in which I listed use cases for system built with Snorkel. It contains:
  - a description of the process for training a text classifier for antisemtic tweets using Snorkel, including:
    - a simple procedure to follow to collect and label data
    - some information on how to define and evaluate labeling functions
    - an example of training the label model and text classifier
