\# DAS Experiment Management Agent



DAS Experiment Management Agent is an AI-agent-driven workflow for managing deep learning experiments in Distributed Acoustic Sensing event recognition and fault diagnosis tasks.



\## Project Motivation



DAS experiments often require repeated adjustment of dataset splitting, data augmentation, model structure, training parameters, and evaluation metrics. Manual experiment tracking can easily become disorganized, especially when preparing reproducible results for research papers.



This project aims to build an experiment management agent that assists with dataset checking, training script generation, metric summarization, and LaTeX table generation.



\## Main Functions



\- Check training, validation, and test set splitting

\- Avoid data leakage after data augmentation

\- Generate PyTorch training script templates

\- Manage experiment configuration files

\- Summarize Accuracy, Precision, Recall, F1-score, inference time, and model parameters

\- Generate LaTeX tables for research papers

\- Generate experiment result analysis text



\## Agent Workflow



1\. Dataset Check Agent  

&#x20;  Checks whether the dataset split is reasonable.



2\. Code Generation Agent  

&#x20;  Generates training and evaluation code templates.



3\. Metric Summary Agent  

&#x20;  Summarizes experiment results and converts them into paper-ready tables.



4\. Writing Agent  

&#x20;  Generates experiment description and analysis paragraphs.



\## Example Use Cases



\- DAS event recognition experiment management

\- Coal mine belt conveyor fault diagnosis experiments

\- MFCC and differential phase feature comparison

\- CNN, ResNet, and dual-stream network comparison

\- Inference time and parameter count reporting



\## Planned Extensions



\- Connect to MiMo API for LLM-driven code generation

\- Add automatic experiment log parsing

\- Add model comparison dashboard

\- Support YAML-based experiment management

