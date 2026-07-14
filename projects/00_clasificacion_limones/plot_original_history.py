"""Reconstruye las curvas guardadas en el notebook original.

Los valores provienen del registro de entrenamiento de cinco épocas incluido
en el notebook 12MBID_04_A_Proyecto_programación_Deep.ipynb.
"""

from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt

EPOCHS = [1, 2, 3, 4, 5]
TRAIN_LOSS = [2.5310, 0.6084, 0.4629, 0.5016, 0.3836]
VAL_LOSS = [0.7090, 0.4878, 0.5914, 0.4878, 0.3507]
TRAIN_ACCURACY = [0.7273, 0.8302, 0.8594, 0.8122, 0.8759]
VAL_ACCURACY = [0.8604, 0.8667, 0.7896, 0.8271, 0.8792]

OUTPUT_DIR = Path(__file__).resolve().parent / "figures"


def plot_accuracy() -> Path:
    """Genera la curva de precisión del entrenamiento original."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(EPOCHS, TRAIN_ACCURACY, marker="o", label="Entrenamiento")
    ax.plot(EPOCHS, VAL_ACCURACY, marker="o", label="Validación")
    ax.set_title("Accuracy por época — CNN de clasificación de limones")
    ax.set_xlabel("Época")
    ax.set_ylabel("Accuracy")
    ax.set_xticks(EPOCHS)
    ax.set_ylim(0.70, 0.91)
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()

    output_path = OUTPUT_DIR / "accuracy_original.png"
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return output_path


def plot_loss() -> Path:
    """Genera la curva de pérdida del entrenamiento original."""
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.plot(EPOCHS, TRAIN_LOSS, marker="o", label="Entrenamiento")
    ax.plot(EPOCHS, VAL_LOSS, marker="o", label="Validación")
    ax.set_title("Loss por época — CNN de clasificación de limones")
    ax.set_xlabel("Época")
    ax.set_ylabel("Categorical cross-entropy")
    ax.set_xticks(EPOCHS)
    ax.grid(alpha=0.25)
    ax.legend()
    fig.tight_layout()

    output_path = OUTPUT_DIR / "loss_original.png"
    fig.savefig(output_path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return output_path


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    accuracy_path = plot_accuracy()
    loss_path = plot_loss()
    print(f"Gráfica de accuracy: {accuracy_path}")
    print(f"Gráfica de loss: {loss_path}")


if __name__ == "__main__":
    main()
