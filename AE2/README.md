# EA2 – Manejo de archivos CSV, JSON y TXT

Kevin Daniel Sepúlveda Giraldo · Analítica de Datos · PREICA2602B020125

## Archivos de origen

| Formato | Dataset | Original |
|---|---|---|
| CSV | [Barrios más baratos para arrendar en Colombia (2026)](https://huggingface.co/datasets/aptologia/barrios-mas-baratos-para-arrendar-colombia-2026/blob/main/data/barrios_mas_baratos_para_arrendar_colombia_2026_datos.csv) | `datos/originales/barrios_mas_baratos_para_arrendar_colombia_2026_datos.csv` |
| JSON | [Colección numismática colombiana](https://huggingface.co/datasets/Vault-of-History/colombian-numismatic-collection/blob/main/colombian-coins.json) | `datos/originales/colombian-coins.json` |

## Estructura

```
AE2/
├── manejador_csv.py           ManejadorCSV (csv.reader / csv.writer)
├── manejador_json.py          ManejadorJSON (json.load / json.dump)
├── generador_resumen_txt.py   GeneradorResumenTXT
├── AE2_manejo_archivos.ipynb
├── resumen.txt
└── datos/
    ├── originales/
    └── modificados/
```

## Cambios

| Archivo | Cambio | Filas / registros |
|---|---|---|
| CSV | Nueva columna `canon_millones` | 145 |
| CSV | `Bogotá` → `Bogotá D.C.` | 34 |
| CSV | Eliminar barrios con menos de 35 avisos | 145 → 125 |
| JSON | Nuevo campo `antiguedad_anios` | 14 |
| JSON | `No longer in circulation` → `Fuera de circulación` | 14 |
| JSON | Eliminar campo `photo` | 14 |

## Ejecución

```bash
python -m pip install -r requirements.txt
cd AE2
jupyter notebook AE2_manejo_archivos.ipynb
```

Ejecutar todas las celdas en orden. Solo usa `csv`, `json` y `pathlib`.

## Uso de IA

Usé Claude (Anthropic) como apoyo para el código y la documentación. Revisé y probé todo lo entregado.
