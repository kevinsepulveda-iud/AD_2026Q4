# AE2 – Manejo de archivos CSV, JSON y TXT

Analítica de Datos – IU Digital de Antioquia · PREICA2602B020125 · AE_Grupo 12

## Archivos de origen (descargados manualmente de Hugging Face)

| Formato | Dataset | URL de origen | Copia local |
|---|---|---|---|
| CSV | Barrios más baratos para arrendar en Colombia (2026) | https://huggingface.co/datasets/aptologia/barrios-mas-baratos-para-arrendar-colombia-2026/blob/main/data/barrios_mas_baratos_para_arrendar_colombia_2026_datos.csv | `datos/originales/barrios_mas_baratos_para_arrendar_colombia_2026_datos.csv` |
| JSON | Colección numismática colombiana | https://huggingface.co/datasets/Vault-of-History/colombian-numismatic-collection/blob/main/colombian-coins.json | `datos/originales/colombian-coins.json` |

Los originales no se modifican. Las versiones modificadas se guardan en `datos/modificados/`.

## Estructura

```
AE2/
├── manejador_csv.py           Clase ManejadorCSV (csv.reader / csv.writer)
├── manejador_json.py          Clase ManejadorJSON (json.load / json.dump)
├── generador_resumen_txt.py   Clase GeneradorResumenTXT (crea resumen.txt)
├── AE2_manejo_archivos.ipynb  Notebook que coordina el flujo
├── resumen.txt                Resumen generado por la ejecución
└── datos/
    ├── originales/            CSV y JSON tal como se descargaron
    └── modificados/           CSV y JSON nuevos con los cambios
```

## Clases y métodos

**`ManejadorCSV`**: `importar()`, `vista_previa()`, `agregar_columna()`, `actualizar_valor()`, `eliminar_filas()`, `guardar()`, `informe()`

**`ManejadorJSON`**: `importar()`, `vista_previa()`, `agregar_campo()`, `actualizar_valor()`, `eliminar_campo()`, `guardar()`, `informe()`

**`GeneradorResumenTXT`**: `agregar_informe()`, `generar_texto()`, `guardar()`

## Modificaciones realizadas

**CSV:** se agrega la columna `canon_millones`, se cambia `Bogotá` por `Bogotá D.C.` y se eliminan los barrios con menos de 35 avisos.

**JSON:** se agrega el campo `antiguedad_anios`, se cambia el estado `No longer in circulation` por `Fuera de circulación` y se elimina el campo `photo`.

## Pasos de ejecución

### Opción 1: automática (GitHub Actions)
Al subir cambios a la carpeta `AE2`, el workflow `.github/workflows/ejecutar-ae2.yml` ejecuta el notebook con
Python 3.12 y guarda en el repositorio el notebook con resultados, los archivos modificados y `resumen.txt`.
También se puede lanzar desde **Actions → Ejecutar AE2 → Run workflow**.

### Opción 2: local
```bash
git clone https://github.com/kevinsepulveda-iud/AD_2026Q4.git
cd AD_2026Q4
python -m pip install -r requirements.txt
cd AE2
jupyter notebook AE2_manejo_archivos.ipynb
```
Ejecutar todas las celdas en orden (**Kernel → Restart & Run All**). Las rutas son relativas a la carpeta `AE2`.
Solo se usan las librerías estándar `csv`, `json` y `pathlib`.

## Uso de inteligencia artificial

De acuerdo con el reglamento estudiantil, declaro que en este trabajo usé **Claude (Anthropic)** como asistente de
inteligencia artificial para:

- Proponer la estructura de las clases y escribir una primera versión del código.
- Revisar errores y probar el flujo completo.
- Redactar la documentación (README y explicaciones de los notebooks).
- Configurar la ejecución automática con GitHub Actions.

Revisé, ejecuté y entiendo todo el código entregado. La elección de los datasets, las transformaciones aplicadas
y los resultados los verifiqué antes de hacer la entrega.
