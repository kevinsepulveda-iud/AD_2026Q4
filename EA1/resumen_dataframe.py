"""Clase para resumir un DataFrame y guardar el resumen en un archivo .txt."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path

import pandas as pd


class ResumenDataFrame:
    """Recibe un DataFrame y genera un resumen legible de su contenido.

    Args:
        df: DataFrame de pandas que se va a resumir.
        titulo: nombre que aparece en el encabezado del resumen.
    """

    def __init__(self, df: pd.DataFrame, titulo: str = "Resumen del DataFrame") -> None:
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Se esperaba un DataFrame de pandas.")
        self.df = df
        self.titulo = titulo

    def dimensiones(self) -> list[str]:
        filas, columnas = self.df.shape
        return [f"Filas: {filas}", f"Columnas: {columnas}"]

    def columnas_y_tipos(self) -> list[str]:
        return [f"- {columna}: {tipo}" for columna, tipo in self.df.dtypes.items()]

    def valores_nulos(self) -> list[str]:
        nulos = self.df.isna().sum()
        lineas = [f"- {columna}: {int(cantidad)}" for columna, cantidad in nulos.items()]
        lineas.append(f"Total de valores nulos: {int(nulos.sum())}")
        return lineas

    def estadisticas(self) -> list[str]:
        numericas = self.df.select_dtypes(include="number")
        if numericas.empty:
            return ["No hay columnas numéricas."]
        return [numericas.describe().round(2).to_string()]

    def generar_texto(self) -> str:
        """Arma todo el resumen como un solo texto."""
        lineas = [
            self.titulo,
            "=" * 70,
            f"Generado: {datetime.now():%Y-%m-%d %H:%M}",
            "",
            "DIMENSIONES",
            *self.dimensiones(),
            f"Filas duplicadas: {int(self.df.duplicated().sum())}",
            "",
            "COLUMNAS Y TIPOS DE DATO",
            *self.columnas_y_tipos(),
            "",
            "VALORES NULOS POR COLUMNA",
            *self.valores_nulos(),
            "",
            "ESTADÍSTICAS DESCRIPTIVAS (columnas numéricas)",
            *self.estadisticas(),
            "",
            "PRIMERAS 5 FILAS",
            self.df.head().to_string(index=False),
        ]
        return "\n".join(lineas) + "\n"

    def guardar(self, ruta: str | Path) -> Path:
        """Guarda el resumen en un archivo .txt y devuelve la ruta."""
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        ruta.write_text(self.generar_texto(), encoding="utf-8")
        return ruta
