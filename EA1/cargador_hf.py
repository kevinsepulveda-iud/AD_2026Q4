"""Clase para obtener un dataset de Hugging Face como DataFrame de pandas."""
from __future__ import annotations

import pandas as pd
from datasets import load_dataset


class CargadorHuggingFace:
    """Se conecta a Hugging Face Datasets y entrega los datos como DataFrame.

    Args:
        nombre_dataset: identificador del dataset en Hugging Face,
            por ejemplo ``"scikit-learn/iris"``.
        split: división que se va a cargar (por defecto ``"train"``).
        configuracion: subconjunto del dataset, solo si tiene varios.
        max_filas: límite de filas a cargar. Sirve para no traer datasets
            demasiado grandes que después no se puedan subir a GitHub.
    """

    def __init__(
        self,
        nombre_dataset: str,
        split: str = "train",
        configuracion: str | None = None,
        max_filas: int | None = None,
    ) -> None:
        if not nombre_dataset:
            raise ValueError("Debes indicar el nombre del dataset.")
        if max_filas is not None and max_filas <= 0:
            raise ValueError("max_filas debe ser mayor que cero.")

        self.nombre_dataset = nombre_dataset
        self.split = split
        self.configuracion = configuracion
        self.max_filas = max_filas
        self.df: pd.DataFrame | None = None

    def cargar(self) -> pd.DataFrame:
        """Descarga el dataset desde Hugging Face y lo devuelve como DataFrame."""
        dataset = load_dataset(
            self.nombre_dataset,
            self.configuracion,
            split=self.split,
        )

        # Si el dataset es grande, solo se toman las primeras filas.
        if self.max_filas is not None:
            dataset = dataset.select(range(min(self.max_filas, len(dataset))))

        self.df = dataset.to_pandas()
        return self.df

    def informacion(self) -> dict[str, str | int | None]:
        """Devuelve los datos básicos de lo que se cargó."""
        if self.df is None:
            raise RuntimeError("Primero llama al método cargar().")
        return {
            "dataset": self.nombre_dataset,
            "split": self.split,
            "configuracion": self.configuracion,
            "filas": len(self.df),
            "columnas": len(self.df.columns),
        }
