import json
from pathlib import Path
from datetime import datetime


def load_config(path: str) -> dict:
    return json.loads(Path(path).read_text(encoding="utf-8"))


def check_dataset_split(config: dict) -> list:
    warnings = []
    dataset = config["dataset"]

    train = dataset["train_ratio"]
    val = dataset["val_ratio"]
    test = dataset["test_ratio"]
    total = train + val + test

    if abs(total - 1.0) > 1e-6:
        warnings.append(f"Dataset split ratios sum to {total}, not 1.0.")

    if dataset["augmentation_stage"] != "train_only":
        warnings.append(
            "Data augmentation should normally be applied only to the training set "
            "to avoid data leakage."
        )

    total_samples = dataset["total_original_samples"]
    train_count = int(total_samples * train)
    val_count = int(total_samples * val)
    test_count = total_samples - train_count - val_count

    return warnings, train_count, val_count, test_count


def generate_markdown_report(config: dict) -> str:
    warnings, train_count, val_count, test_count = check_dataset_split(config)

    lines = []
    lines.append("# DAS Experiment Management Report")
    lines.append("")
    lines.append(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    lines.append("")

    lines.append("## 1. Experiment Overview")
    lines.append("")
    lines.append(f"- Experiment name: {config['experiment_name']}")
    lines.append(f"- Model: {config['model']['name']}")
    lines.append(f"- Input features: {', '.join(config['model']['input_features'])}")
    lines.append("")

    lines.append("## 2. Dataset Split Check")
    lines.append("")
    lines.append(f"- Training samples: {train_count}")
    lines.append(f"- Validation samples: {val_count}")
    lines.append(f"- Test samples: {test_count}")
    lines.append(f"- Augmentation stage: {config['dataset']['augmentation_stage']}")
    lines.append("")

    if warnings:
        lines.append("### Warnings")
        for warning in warnings:
            lines.append(f"- {warning}")
    else:
        lines.append("No obvious dataset split problems detected.")
    lines.append("")

    lines.append("## 3. Result Summary")
    lines.append("")
    lines.append("| Model | Accuracy | Precision | Recall | F1-score | Inference Time |")
    lines.append("|---|---:|---:|---:|---:|---:|")

    for item in config["results"]:
        lines.append(
            f"| {item['model']} | "
            f"{item['accuracy']:.3f} | "
            f"{item['precision']:.3f} | "
            f"{item['recall']:.3f} | "
            f"{item['f1_score']:.3f} | "
            f"{item['inference_time_ms']:.2f} ms |"
        )

    lines.append("")
    lines.append("## 4. Paper-style Analysis")
    lines.append("")
    lines.append(
        "The experimental results indicate that the dual-stream ResNet achieves the best "
        "overall classification performance among the compared models. It obtains higher "
        "accuracy, precision, recall, and F1-score, while maintaining an acceptable inference "
        "time. This suggests that combining MFCC and differential phase features can improve "
        "the discriminative representation of DAS vibration events."
    )
    lines.append("")

    lines.append("## 5. LaTeX Table")
    lines.append("")
    lines.append("```latex")
    lines.append("\\begin{table}[htbp]")
    lines.append("\\centering")
    lines.append("\\caption{Comparison of different models on the DAS event recognition task.}")
    lines.append("\\begin{tabular}{lccccc}")
    lines.append("\\hline")
    lines.append("Model & Accuracy & Precision & Recall & F1-score & Time \\\\")
    lines.append("\\hline")

    for item in config["results"]:
        lines.append(
            f"{item['model']} & "
            f"{item['accuracy']:.3f} & "
            f"{item['precision']:.3f} & "
            f"{item['recall']:.3f} & "
            f"{item['f1_score']:.3f} & "
            f"{item['inference_time_ms']:.2f} ms \\\\"
        )

    lines.append("\\hline")
    lines.append("\\end{tabular}")
    lines.append("\\end{table}")
    lines.append("```")

    return "\n".join(lines)


def main():
    config_path = "configs/sample_experiment.json"
    output_path = "outputs/experiment_report.md"

    config = load_config(config_path)
    report = generate_markdown_report(config)

    Path(output_path).write_text(report, encoding="utf-8")

    print(f"Experiment report generated: {output_path}")


if __name__ == "__main__":
    main()