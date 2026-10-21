"""Clase para importar, modificar y guardar archivos CSV con el módulo csv."""
from __future__ import annotations

import csv
from pathlib import Path
from typing import Callable


class ManejadorCSV:
    """Maneja un archivo CSV: lo importa con csv.reader, lo modifica y lo
    guarda en un archivo nuevo con csv.writer, conservando el original.

    Args:
        ruta_origen: ruta local del CSV descargado.
        url_origen: URL de donde se descargó el archivo.
    """

    def __init__(self, ruta_origen: str | Path, url_origen: str) -> None:
        self.ruta_origen = Path(ruta_origen)
        self.url_origen = url_origen
        self.ruta_salida: Path | None = None
        self.encabezados: list[str] = []
        self.filas: list[list[str]] = []
        self.registros_importados = 0
        self.modificaciones: list[str] = []
        self.metodos_usados: list[str] = []

    def importar(self) -> int:
        """Lee el CSV con csv.reader. La primera fila son los encabezados."""
        with open(self.ruta_origen, mode="r", encoding="utf-8", newline="") as archivo:
            lector = csv.reader(archivo)
            self.encabezados = next(lector)
            self.filas = [fila for fila in lector if fila]
        self.registros_importados = len(self.filas)
        self._registrar_metodo("importar")
        return self.registros_importados

    def vista_previa(self, cantidad: int = 5) -> list[dict[str, str]]:
        """Devuelve las primeras filas como diccionarios para mostrarlas."""
        return [dict(zip(self.encabezados, fila)) for fila in self.filas[:cantidad]]

    def agregar_columna(self, nombre: str, calcular: Callable[[dict[str, str]], object]) -> None:
        """Agrega una columna nueva calculada a partir de cada fila."""
        if nombre in self.encabezados:
            raise ValueError(f"La columna '{nombre}' ya existe.")
        for fila in self.filas:
            registro = dict(zip(self.encabezados, fila))
            fila.append(str(calcular(registro)))
        self.encabezados.append(nombre)
        self.modificaciones.append(f"Se agregó la columna '{nombre}' a {len(self.filas)} filas.")
        self._registrar_metodo("agregar_columna")

    def actualizar_valor(self, columna: str, valor_actual: str, valor_nuevo: str) -> int:
        """Reemplaza un valor en una columna y devuelve cuántas filas cambiaron."""
        indice = self._indice(columna)
        cambios = 0
        for fila in self.filas:
            if fila[indice] == valor_actual:
                fila[indice] = valor_nuevo
                cambios += 1
        self.modificaciones.append(
            f"En la columna '{columna}' se cambió '{valor_actual}' por '{valor_nuevo}' ({cambios} filas)."
        )
        self._registrar_metodo("actualizar_valor")
        return cambios

    def eliminar_filas(self, condicion: Callable[[dict[str, str]], bool], descripcion: str) -> int:
        """Elimina las filas que cumplen la condición y devuelve cuántas se quitaron."""
        antes = len(self.filas)
        self.filas = [
            fila for fila in self.filas
            if not condicion(dict(zip(self.encabezados, fila)))
        ]
        eliminadas = antes - len(self.filas)
        self.modificaciones.append(f"Se eliminaron {eliminadas} filas: {descripcion}.")
        self._registrar_metodo("eliminar_filas")
        return eliminadas

    def guardar(self, ruta_salida: str | Path) -> Path:
        """Escribe un CSV nuevo con csv.writer, incluyendo los encabezados."""
        self.ruta_salida = Path(ruta_salida)
        if self.ruta_salida.resolve() == self.ruta_origen.resolve():
            raise ValueError("Usa un nombre nuevo para no sobrescribir el original.")
        self.ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        with open(self.ruta_salida, mode="w", encoding="utf-8", newline="") as archivo:
            escritor = csv.writer(archivo)
            escritor.writerow(self.encabezados)
            escritor.writerows(self.filas)
        self._registrar_metodo("guardar")
        return self.ruta_salida

    def informe(self) -> dict:
        """Datos de lo que hizo la clase, para el resumen .txt."""
        return {
            "tipo": "CSV",
            "clase": type(self).__name__,
            "url_origen": self.url_origen,
            "archivo_importado": self.ruta_origen.as_posix(),
            "archivo_guardado": self.ruta_salida.as_posix() if self.ruta_salida else "sin guardar",
            "registros_importados": self.registros_importados,
            "registros_guardados": len(self.filas),
            "columnas_finales": list(self.encabezados),
            "modificaciones": list(self.modificaciones),
            "metodos_usados": list(self.metodos_usados),
        }

    def _indice(self, columna: str) -> int:
        if columna not in self.encabezados:
            raise KeyError(f"No existe la columna '{columna}'.")
        return self.encabezados.index(columna)

    def _registrar_metodo(self, nombre: str) -> None:
        if nombre not in self.metodos_usados:
            self.metodos_usados.append(nombre)
