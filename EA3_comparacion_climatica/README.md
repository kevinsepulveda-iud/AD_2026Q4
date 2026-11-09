# EA3 – Comparación climática: Medellín vs. Madrid (2019)

| Archivo | Contenido |
|---|---|
| `EA3_Sepulveda_Kevin.ipynb` | Notebook con la carga, revisión, análisis con NumPy, gráficas e interpretación |
| `datos/medellin.csv` | Datos diarios 2019 de la estación Aeropuerto Olaya Herrera (Medellín) |
| `datos/madrid.csv` | Datos diarios 2019 de la estación Madrid Retiro (España) |

## Datos de origen

Los dos archivos son de [NOAA NCEI – GHCN-Daily](https://www.ncei.noaa.gov/products/land-based-station/global-historical-climatology-network-daily), descargados con el servicio `https://www.ncei.noaa.gov/access/services/data/v1` (`dataset=daily-summaries`, `units=metric`, del 2019-01-01 al 2019-12-31).

| Ciudad | Estación | Días | Faltan PRCP | Faltan TAVG |
|---|---|---|---|---|
| Medellín | `COM00080110` | 365 | 71 | 0 |
| Madrid | `SP000003195` | 365 | 1 | 9 |

Variables: `TAVG` y `TMIN` en °C, `PRCP` en mm.

## Cambios que hice a los datos

- Campos vacíos → `np.nan` (nunca 0).
- Fechas de texto → `datetime`; mediciones de texto → `float`.
- No borré filas: para comparar día a día uso solo las fechas con dato en ambas ciudades.
- No usé `TMAX` porque Medellín casi no la tiene en 2019.

## Ejecución

```bash
python -m pip install -r requirements.txt
cd EA3_comparacion_climatica
jupyter nbconvert --to notebook --execute --inplace EA3_Sepulveda_Kevin.ipynb
```

Si falta algún CSV, el notebook lo vuelve a descargar de NOAA. También se ejecuta con GitHub Actions cuando subo cambios a esta carpeta.

Usé Claude (Anthropic) como apoyo para el código y la documentación. Revisé y probé todo lo entregado.
