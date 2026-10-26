# AD_2026Q4 – Analítica de Datos

Kevin Daniel Sepúlveda Giraldo · IU Digital de Antioquia · PREICA2602B020125

| Carpeta | Actividad |
|---|---|
| [`EA1/`](EA1) | EA1 – Carga y creación de dataset |
| [`AE2/`](AE2) | EA2 – Manejo de archivos y clases |

## EA1 – Carga y creación de dataset

Dataset: [`aptologia/casa-vs-apartamento-precio-m2-ciudades-colombia-2026`](https://huggingface.co/datasets/aptologia/casa-vs-apartamento-precio-m2-ciudades-colombia-2026) (precio por m² de casa y apartamento en 38 ciudades de Colombia).

| Archivo | Contenido |
|---|---|
| `cargador_hf.py` | Clase `CargadorHuggingFace`: dataset de Hugging Face → DataFrame |
| `resumen_dataframe.py` | Clase `ResumenDataFrame`: DataFrame → resumen `.txt` |
| `EA1_carga_y_resumen.ipynb` | Une las dos clases y aplica 4 transformaciones |
| `resultados/resumen_casa_vs_apartamento.txt` | Resumen del DataFrame transformado |

## Ejecución

```bash
git clone https://github.com/kevinsepulveda-iud/AD_2026Q4.git
cd AD_2026Q4
python -m pip install -r requirements.txt
```

Abrir el notebook de cada carpeta y ejecutar todas las celdas (Python 3.12).
Los notebooks también se ejecutan con GitHub Actions cada vez que subo cambios (pestaña **Actions**).

## Uso de IA

Usé Claude (Anthropic) como apoyo para el código y la documentación. Revisé y probé todo lo entregado.
