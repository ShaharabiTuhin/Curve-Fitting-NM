"""Student Performance Prediction Using Curve Fitting Techniques.

This script demonstrates an undergraduate-level numerical methods project
using polynomial curve fitting (least squares) to predict GPA.
"""

from __future__ import annotations

from pathlib import Path
from typing import Dict, Tuple

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


ROOT_DIR = Path(__file__).resolve().parent.parent
DATA_FILE = ROOT_DIR / "data" / "student_performance.csv"
OUTPUT_DIR = ROOT_DIR / "outputs"


def load_dataset(path: Path = DATA_FILE) -> pd.DataFrame:
    """Load and validate the project dataset."""
    df = pd.read_csv(path)
    required_cols = [
        "Study_Hours",
        "Attendance_Percentage",
        "Assignment_Marks",
        "GPA",
    ]

    missing_cols = [col for col in required_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Missing required columns: {missing_cols}")

    return df


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Create a weighted study index from study-related features.

    Study Index = 0.5*(Study Hours) + 0.3*(Attendance/10) + 0.2*(Assignment/10)
    """
    processed = df.copy()
    processed["Study_Index"] = (
        0.5 * processed["Study_Hours"]
        + 0.3 * (processed["Attendance_Percentage"] / 10)
        + 0.2 * (processed["Assignment_Marks"] / 10)
    )
    return processed


def fit_polynomial_curve(
    x: np.ndarray, y: np.ndarray, degree: int = 2
) -> np.ndarray:
    """Fit polynomial coefficients using least squares (numpy.polyfit)."""
    if degree < 1:
        raise ValueError("Degree must be at least 1")
    return np.polyfit(x, y, degree)


def predict_gpa(coefficients: np.ndarray, study_index: np.ndarray) -> np.ndarray:
    """Predict GPA values from fitted polynomial coefficients."""
    return np.polyval(coefficients, study_index)


def calculate_errors(actual: np.ndarray, predicted: np.ndarray) -> Dict[str, float]:
    """Return common error metrics for model evaluation."""
    residuals = actual - predicted
    mse = float(np.mean(residuals**2))
    rmse = float(np.sqrt(mse))
    mae = float(np.mean(np.abs(residuals)))

    ss_total = float(np.sum((actual - np.mean(actual)) ** 2))
    ss_res = float(np.sum(residuals**2))
    r2 = 1 - ss_res / ss_total if ss_total > 0 else 0.0

    return {"MSE": mse, "RMSE": rmse, "MAE": mae, "R2": r2}


def create_visualizations(
    x: np.ndarray,
    y_actual: np.ndarray,
    y_pred: np.ndarray,
    coefficients: np.ndarray,
    output_dir: Path = OUTPUT_DIR,
) -> Tuple[Path, Path, Path, Path]:
    """Generate and save required project graphs."""
    output_dir.mkdir(parents=True, exist_ok=True)

    # Smooth curve points
    x_curve = np.linspace(x.min(), x.max(), 200)
    y_curve = np.polyval(coefficients, x_curve)

    # 1) Scatter + fitted curve
    scatter_curve_path = output_dir / "scatter_fitted_curve.png"
    plt.figure(figsize=(8, 5))
    plt.scatter(x, y_actual, color="royalblue", label="Actual GPA")
    plt.plot(x_curve, y_curve, color="crimson", linewidth=2, label="Fitted Polynomial Curve")
    plt.xlabel("Study Index")
    plt.ylabel("GPA")
    plt.title("Scatter Plot and Fitted Curve")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(scatter_curve_path, dpi=150)
    plt.close()

    # 2) Prediction graph (actual vs predicted)
    prediction_path = output_dir / "prediction_comparison.png"
    plt.figure(figsize=(8, 5))
    plt.plot(y_actual, marker="o", label="Actual GPA", color="forestgreen")
    plt.plot(y_pred, marker="x", label="Predicted GPA", color="darkorange")
    plt.xlabel("Student Record Index")
    plt.ylabel("GPA")
    plt.title("Actual vs Predicted GPA")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(prediction_path, dpi=150)
    plt.close()

    # 3) Error visualization (residuals)
    residuals = y_actual - y_pred
    error_path = output_dir / "residual_errors.png"
    plt.figure(figsize=(8, 5))
    plt.axhline(0, color="black", linewidth=1)
    plt.bar(range(len(residuals)), residuals, color="slateblue")
    plt.xlabel("Student Record Index")
    plt.ylabel("Residual (Actual - Predicted)")
    plt.title("Residual Error Visualization")
    plt.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    plt.savefig(error_path, dpi=150)
    plt.close()

    # 4) Direct fitted curve graph
    fitted_curve_path = output_dir / "fitted_curve_only.png"
    sorted_idx = np.argsort(x)
    plt.figure(figsize=(8, 5))
    plt.plot(x[sorted_idx], y_actual[sorted_idx], "o", label="Observed GPA", color="teal")
    plt.plot(x_curve, y_curve, "-", linewidth=2, label="Polynomial Fit", color="maroon")
    plt.xlabel("Study Index")
    plt.ylabel("GPA")
    plt.title("Fitted Curve for GPA Prediction")
    plt.legend()
    plt.grid(alpha=0.3)
    plt.tight_layout()
    plt.savefig(fitted_curve_path, dpi=150)
    plt.close()

    return scatter_curve_path, fitted_curve_path, prediction_path, error_path


def run_project() -> None:
    """Execute the full workflow for the curve fitting project."""
    df = load_dataset()
    data = preprocess_data(df)

    x = data["Study_Index"].to_numpy()
    y = data["GPA"].to_numpy()

    coefficients = fit_polynomial_curve(x, y, degree=2)
    y_pred = predict_gpa(coefficients, x)
    metrics = calculate_errors(y, y_pred)

    graph_paths = create_visualizations(x, y, y_pred, coefficients)

    print("\n=== Student Performance Prediction Using Curve Fitting ===")
    print(f"Dataset size: {len(data)} records")
    print("Polynomial degree: 2")
    print("\nModel Equation:")
    print(
        f"GPA = {coefficients[0]:.4f}(Study_Index)^2 + "
        f"{coefficients[1]:.4f}(Study_Index) + {coefficients[2]:.4f}"
    )

    print("\nError Metrics:")
    for metric, value in metrics.items():
        print(f"- {metric}: {value:.4f}")

    # Example prediction
    sample_study_hours = 7.0
    sample_attendance = 92
    sample_assignment = 88
    sample_index = (
        0.5 * sample_study_hours
        + 0.3 * (sample_attendance / 10)
        + 0.2 * (sample_assignment / 10)
    )
    sample_gpa_pred = predict_gpa(coefficients, np.array([sample_index]))[0]

    print("\nSample Prediction:")
    print(
        f"Input -> Study Hours: {sample_study_hours}, Attendance: {sample_attendance}%, "
        f"Assignment Marks: {sample_assignment}"
    )
    print(f"Predicted GPA: {sample_gpa_pred:.2f}")

    print("\nGenerated Graph Files:")
    for path in graph_paths:
        print(f"- {path}")


if __name__ == "__main__":
    run_project()
