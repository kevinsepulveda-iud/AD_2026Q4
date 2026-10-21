"""Clase para generar el resumen .txt con lo que hicieron las otras clases."""
from __future__ import annotations

from datetime import datetime
from pathlib import Path


class GeneradorResumenTXT:
    """Recibe los informes de ManejadorCSV y ManejadorJSON y escribe un resumen.

    Args:
        titulo: encabezado del resumen.
        urls_origen: diccionario con las URL de origen de cada archivo.
    """

    def __init__(self, titulo: str, urls_origen: dict[str, str]) -> None:
        self.titulo = titulo
        self.urls_origen = urls_origen
        self.informes: list[dict] = []

    def agregar_informe(self, informe: dict) -> None:
        """Recibe el resultado de una de las clases (su método informe())."""
        self.informes.append(informe)

    def generar_texto(self) -> str:
        """Arma el contenido completo del resumen con los resultados reales."""
        lineas = [
            self.titulo,
            "=" * 70,
            f"Generado: {datetime.now():%Y-%m-%d %H:%M}",
            "",
            "URL DE ORIGEN",
            *[f"- {tipo}: {url}" for tipo, url in self.urls_origen.items()],
        ]

        for informe in self.informes:
            lineas += [
                "",
                f"ARCHIVO {informe['tipo']} - clase {informe['clase']}",
                "-" * 70,
                f"URL de origen:        {informe['url_origen']}",
                f"Archivo importado:    {informe['archivo_importado']}",
                f"Archivo guardado:     {informe['archivo_guardado']}",
                f"Registros importados: {informe['registros_importados']}",
                f"Registros guardados:  {informe['registros_guardados']}",
                f"Métodos utilizados:   {', '.join(informe['metodos_usados'])}",
                "Modificaciones realizadas:",
                *[f"  {i}. {cambio}" for i, cambio in enumerate(informe["modificaciones"], start=1)],
            ]
            if "columnas_finales" in informe:
                lineas.append(f"Columnas finales:     {', '.join(informe['columnas_finales'])}")

        total = sum(informe["registros_importados"] for informe in self.informes)
        lineas += [
            "",
            "TOTALES",
            "-" * 70,
            f"Archivos procesados: {len(self.informes)}",
            f"Registros procesados en total: {total}",
            f"Clases utilizadas: {', '.join(i['clase'] for i in self.informes)}, {type(self).__name__}",
        ]
        return "\n".join(lineas) + "\n"

    def guardar(self, ruta: str | Path = "resumen.txt") -> Path:
        """Escribe el resumen en un archivo .txt y devuelve la ruta."""
        if not self.informes:
            raise RuntimeError("No hay informes. Usa agregar_informe() primero.")
        ruta = Path(ruta)
        ruta.parent.mkdir(parents=True, exist_ok=True)
        with open(ruta, mode="w", encoding="utf-8") as archivo:
            archivo.write(self.generar_texto())
        return ruta
