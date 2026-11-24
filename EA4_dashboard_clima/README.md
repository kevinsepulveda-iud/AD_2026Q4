# EA4 – Dashboard: ¿cuándo se parece Madrid a Medellín?

**Dashboard publicado:** https://kevinsepulveda-iud.github.io/AD_2026Q4/EA4_dashboard_clima/

## Pregunta

¿En qué meses de 2019 la temperatura media diaria de Madrid se pareció a la de Medellín?

En la EA3 encontré que Medellín casi no cambia de temperatura en el año y Madrid sí. Ahora quiero saber en qué época
las dos ciudades se acercan, por ejemplo para saber cuándo un paisa sentiría en Madrid un clima parecido al de su casa.

## Datos

Reutilizo los mismos archivos de la EA3 (no los copié, el dashboard los lee de `../EA3_comparacion_climatica/datos/`):

| Archivo | Estación | Qué es cada fila |
|---|---|---|
| `medellin.csv` | Olaya Herrera, `COM00080110` | un día de 2019 |
| `madrid.csv` | Madrid Retiro, `SP000003195` | un día de 2019 |

Fuente: NOAA NCEI, GHCN-Daily (`daily-summaries`, unidades métricas). Uso `TAVG` (°C) y `PRCP` (mm).
No son datos simulados.

**Preparación**
- Uní las dos ciudades por fecha (365 días).
- Un campo vacío es un dato que no existe: queda como vacío, **no como 0**. Por eso solo comparo los días con TAVG en
  las dos ciudades: 356 días (Madrid no tiene TAVG en 9 días).
- Un día es *parecido* si `|TAVG Madrid − TAVG Medellín| ≤ tolerancia`. La tolerancia la elige el usuario
  (de 0,5 a 5 °C; por defecto 2 °C).
- Con el filtro de días secos, un día solo cuenta si Madrid tuvo menos de 1 mm. Si Madrid no tiene dato de lluvia
  ese día, no cuenta (no supongo que no llovió).

## Qué hace el dashboard

- Filtros: tolerancia, mes inicial y final, y solo días secos en Madrid.
- Indicadores: días comparables, días parecidos (y su %), mes con más días parecidos y diferencia media.
- Gráfica diaria de las dos ciudades con los días parecidos marcados en amarillo.
- Barras de días parecidos por mes.
- Tabla con cada día parecido.
- Recuadro de calidad de datos con los faltantes.

## Comprobación fuera del dashboard

`EA4_verificacion_Excel.xlsx` tiene los mismos datos con fórmulas (`=D2-C2`, `=ABS(E2)<=$J$2`, `COUNTIFS`).
Con tolerancia ±2 °C:

| Resultado | Dashboard | Excel |
|---|---|---|
| Días comparables | 356 | 356 |
| Días parecidos en el año | 47 | 47 |
| Días parecidos en agosto | 16 | 16 |
| Diferencia media | −8,5 °C | −8,5 °C |

## Mi rúbrica (100 puntos)

| # | Criterio | Logro completo | Logro parcial | Puntos | Me asigno |
|---|---|---|---|---|---|
| 1 | **Pregunta y datos** | La pregunta se puede responder con los datos, se dice la fuente (NOAA, estaciones) y qué es cada fila, y se explica una decisión de preparación (faltantes como vacío, no como 0). | Falta la fuente, qué representa cada fila o la decisión de preparación. | 20 | |
| 2 | **Filtros funcionan** | Al cambiar la tolerancia, los meses o el filtro de días secos, cambian los cuatro indicadores, las dos gráficas y la tabla. Si escojo solo agosto, la gráfica diaria muestra únicamente días de agosto. | Algún filtro no actualiza todas las partes. | 25 | |
| 3 | **Hallazgo con cifras** | Se presenta al menos un hallazgo con cifras (p. ej. "con ±2 °C hubo 47 días parecidos y 16 fueron en agosto") y se dice qué responde de la pregunta. | El hallazgo no tiene cifras o no se relaciona con la pregunta. | 15 | |
| 4 | **Verificación y limitación** | Se muestra en Excel al menos un resultado y coincide con el dashboard. Se dice al menos una limitación (un solo año, una estación por ciudad, faltantes). | Se verifica, pero no coincide o no se explica; o falta la limitación. | 20 | |
| 5 | **Uso de IA** | Se muestra un ejemplo concreto: qué le pedí a la IA, qué generó, qué probé y qué decidí conservar, corregir o descartar. | Se dice que se usó IA pero sin un ejemplo concreto. | 15 | |
| 6 | **Explicación y video** | El video dura entre 5 y 8 minutos, se ve la demostración y se entiende la explicación. | El video se pasa del tiempo o alguna parte no se entiende. | 5 | |
| | **Total** | | | **100** | |

## Uso de IA

Construí el dashboard con Claude (IA) por *vibe coding*: le describí la pregunta y lo que quería ver, me generó una
primera versión en HTML con Chart.js, la probé y fui ajustando. El ejemplo concreto lo cuento en el video.

---
Kevin Daniel Sepúlveda Giraldo · Analítica de Datos (PREICA2602B020125) · IU Digital de Antioquia
