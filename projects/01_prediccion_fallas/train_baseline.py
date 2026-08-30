"""Modelo base reproducible para predicción de fallas industriales.

Este script genera datos sintéticos, entrena una regresión logística y reporta
métricas apropiadas para un problema desbalanceado. Posteriormente se reemplazará
la generación sintética por un cargador de datos industriales documentado.
"""

from __future__ import annotations

import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    average_precision_score,
    classification_report,
    confusion_matrix,
    roc_auc_score,
)
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

RANDOM_STATE = 42
OUTPUT_DIR = Path(__file__).resolve().parent / "outputs"


def generate_synthetic_data(n_samples: int = 5_000) -> pd.DataFrame:
    """Genera datos sintéticos con una relación plausible entre condición y falla."""
    rng = np.random.default_rng(RANDOM_STATE)

    temperature_c = rng.normal(68, 11, n_samples)
    vibration_rms = np.clip(rng.gamma(2.2, 1.1, n_samples), 0, None)
    current_a = rng.normal(92, 16, n_samples)
    operating_hours = rng.uniform(100, 25_000, n_samples)
    power_factor = np.clip(rng.normal(0.91, 0.045, n_samples), 0.65, 1.0)

    risk_score = (
        0.095 * (temperature_c - 72)
        + 0.62 * (vibration_rms - 3.0)
        + 0.018 * (current_a - 100)
        + 0.000075 * (operating_hours - 12_000)
        - 5.0 * (power_factor - 0.90)
        - 3.1
    )
    probability = 1.0 / (1.0 + np.exp(-risk_score))
    failure = rng.binomial(1, probability)

    return pd.DataFrame(
        {
            "temperature_c": temperature_c,
            "vibration_rms": vibration_rms,
            "current_a": current_a,
            "operating_hours": operating_hours,
            "power_factor": power_factor,
            "failure": failure,
        }
    )


def build_pipeline(feature_names: list[str]) -> Pipeline:
    """Construye un pipeline que evita procesar los datos fuera del entrenamiento."""
    preprocessor = ColumnTransformer(
        transformers=[
            (
                "numeric",
                Pipeline(
                    steps=[
                        ("imputer", SimpleImputer(strategy="median")),
                        ("scaler", StandardScaler()),
                    ]
                ),
                feature_names,
            )
        ]
    )

    return Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "classifier",
                LogisticRegression(
                    class_weight="balanced",
                    max_iter=1_000,
                    random_state=RANDOM_STATE,
                ),
            ),
        ]
    )


def main() -> None:
    data = generate_synthetic_data()
    feature_names = [column for column in data.columns if column != "failure"]

    x_train, x_test, y_train, y_test = train_test_split(
        data[feature_names],
        data["failure"],
        test_size=0.25,
        stratify=data["failure"],
        random_state=RANDOM_STATE,
    )

    model = build_pipeline(feature_names)
    model.fit(x_train, y_train)

    probabilities = model.predict_proba(x_test)[:, 1]
    predictions = (probabilities >= 0.5).astype(int)

    metrics = {
        "failure_rate_test": float(y_test.mean()),
        "roc_auc": float(roc_auc_score(y_test, probabilities)),
        "pr_auc": float(average_precision_score(y_test, probabilities)),
        "confusion_matrix": confusion_matrix(y_test, predictions).tolist(),
        "classification_report": classification_report(
            y_test, predictions, output_dict=True, zero_division=0
        ),
    }

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / "baseline_metrics.json"
    output_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

    print(json.dumps(metrics, indent=2))
    print(f"\nMétricas guardadas en: {output_path}")


if __name__ == "__main__":
    main()
