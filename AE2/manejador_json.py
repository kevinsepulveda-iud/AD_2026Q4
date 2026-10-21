"""Clase para importar, modificar y guardar archivos JSON con el módulo json."""
from __future__ import annotations

import copy
import json
from pathlib import Path
from typing import Callable


class ManejadorJSON:
    """Maneja un archivo JSON que contiene una lista de registros: lo importa
    con json.load, lo modifica y lo guarda en un archivo nuevo con json.dump.

    Args:
        ruta_origen: ruta local del JSON descargado.
        url_origen: URL de donde se descargó el archivo.
    """

    def __init__(self, ruta_origen: str | Path, url_origen: str) -> None:
        self.ruta_origen = Path(ruta_origen)
        self.url_origen = url_origen
        self.ruta_salida: Path | None = None
        self.registros: list[dict] = []
        self.registros_importados = 0
        self.modificaciones: list[str] = []
        self.metodos_usados: list[str] = []

    def importar(self) -> int:
        """Lee el archivo con json.load. Se espera una lista de objetos."""
        with open(self.ruta_origen, mode="r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        if not isinstance(datos, list):
            raise ValueError("El JSON debe contener una lista de registros.")
        self.registros = datos
        self.registros_importados = len(datos)
        self._registrar_metodo("importar")
        return self.registros_importados

    def vista_previa(self, cantidad: int = 3, campos: list[str] | None = None) -> list[dict]:
        """Devuelve una copia de los primeros registros (opcionalmente solo algunos campos)."""
        muestra = self.registros[:cantidad]
        if campos:
            return [{campo: registro.get(campo) for campo in campos} for registro in muestra]
        return copy.deepcopy(muestra)

    def agregar_campo(self, nombre: str, calcular: Callable[[dict], object]) -> None:
        """Agrega un campo nuevo a cada registro, calculado a partir del registro."""
        for registro in self.registros:
            registro[nombre] = calcular(registro)
        self.modificaciones.append(f"Se agregó el campo '{nombre}' a {len(self.registros)} registros.")
        self._registrar_metodo("agregar_campo")

    def actualizar_valor(self, campo: str, valor_actual: object, valor_nuevo: object) -> int:
        """Reemplaza un valor en un campo y devuelve cuántos registros cambiaron."""
        cambios = 0
        for registro in self.registros:
            if registro.get(campo) == valor_actual:
                registro[campo] = valor_nuevo
                cambios += 1
        self.modificaciones.append(
            f"En el campo '{campo}' se cambió '{valor_actual}' por '{valor_nuevo}' ({cambios} registros)."
        )
        self._registrar_metodo("actualizar_valor")
        return cambios

    def eliminar_campo(self, campo: str) -> int:
        """Quita un campo de todos los registros y devuelve en cuántos estaba."""
        quitados = sum(1 for registro in self.registros if registro.pop(campo, None) is not None)
        self.modificaciones.append(f"Se eliminó el campo '{campo}' de {quitados} registros.")
        self._registrar_metodo("eliminar_campo")
        return quitados

    def guardar(self, ruta_salida: str | Path) -> Path:
        """Escribe un JSON nuevo con json.dump, legible y con tildes."""
        self.ruta_salida = Path(ruta_salida)
        if self.ruta_salida.resolve() == self.ruta_origen.resolve():
            raise ValueError("Usa un nombre nuevo para no sobrescribir el original.")
        self.ruta_salida.parent.mkdir(parents=True, exist_ok=True)
        with open(self.ruta_salida, mode="w", encoding="utf-8") as archivo:
            json.dump(self.registros, archivo, ensure_ascii=False, indent=2)
        self._registrar_metodo("guardar")
        return self.ruta_salida

    def informe(self) -> dict:
        """Datos de lo que hizo la clase, para el resumen .txt."""
        return {
            "tipo": "JSON",
            "clase": type(self).__name__,
            "url_origen": self.url_origen,
            "archivo_importado": self.ruta_origen.as_posix(),
            "archivo_guardado": self.ruta_salida.as_posix() if self.ruta_salida else "sin guardar",
            "registros_importados": self.registros_importados,
            "registros_guardados": len(self.registros),
            "modificaciones": list(self.modificaciones),
            "metodos_usados": list(self.metodos_usados),
        }

    def _registrar_metodo(self, nombre: str) -> None:
        if nombre not in self.metodos_usados:
            self.metodos_usados.append(nombre)
