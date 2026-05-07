# DAS Experiment Management Report

Generated at: 2026-05-07 19:28:30

## 1. Experiment Overview

- Experiment name: das_event_recognition_baseline
- Model: dual_stream_resnet
- Input features: MFCC, differential_phase

## 2. Dataset Split Check

- Training samples: 630
- Validation samples: 135
- Test samples: 135
- Augmentation stage: train_only

No obvious dataset split problems detected.

## 3. Result Summary

| Model | Accuracy | Precision | Recall | F1-score | Inference Time |
|---|---:|---:|---:|---:|---:|
| CNN | 0.950 | 0.948 | 0.950 | 0.949 | 3.20 ms |
| ResNet | 0.970 | 0.969 | 0.970 | 0.969 | 4.60 ms |
| Dual-stream ResNet | 0.982 | 0.981 | 0.982 | 0.981 | 5.07 ms |

## 4. Paper-style Analysis

The experimental results indicate that the dual-stream ResNet achieves the best overall classification performance among the compared models. It obtains higher accuracy, precision, recall, and F1-score, while maintaining an acceptable inference time. This suggests that combining MFCC and differential phase features can improve the discriminative representation of DAS vibration events.

## 5. LaTeX Table

```latex
\begin{table}[htbp]
\centering
\caption{Comparison of different models on the DAS event recognition task.}
\begin{tabular}{lccccc}
\hline
Model & Accuracy & Precision & Recall & F1-score & Time \\
\hline
CNN & 0.950 & 0.948 & 0.950 & 0.949 & 3.20 ms \\
ResNet & 0.970 & 0.969 & 0.970 & 0.969 & 4.60 ms \\
Dual-stream ResNet & 0.982 & 0.981 & 0.982 & 0.981 & 5.07 ms \\
\hline
\end{tabular}
\end{table}
```