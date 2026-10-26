# AD_2026Q4 – Analítica de Datos

Repositorio del curso **Analítica de Datos** – IU Digital de Antioquia
Grupo: PREICA2602B020125 · AE_Grupo 12 · Docentes: Andrés Felipe Callejas y Mateo del Gallego

## Contenido

| Carpeta | Actividad |
|---|---|
| `EA1/` | Evidencia de Aprendizaje 1: carga y creación de dataset desde Hugging Face |
| `AE2/` | Evidencia de Aprendizaje 2: manejo de archivos CSV, JSON y TXT |

## EA1 – Carga y creación de dataset

| Archivo | Qué hace |
|---|---|
| `EA1/cargador_hf.py` | Clase `CargadorHuggingFace`: se conecta a Hugging Face y devuelve el dataset como DataFrame de pandas. |
| `EA1/resumen_dataframe.py` | Clase `ResumenDataFrame`: recibe un DataFrame y guarda un resumen en `.txt` (filas, columnas, tipos, nulos y estadísticas). |
| `EA1/EA1_carga_y_resumen.ipynb` | Notebook que coordina las dos clases y aplica 4 transformaciones al DataFrame. |
| `EA1/resultados/resumen_casa_vs_apartamento.txt` | Resumen generado a partir del DataFrame transformado. |

**Dataset:** [`aptologia/casa-vs-apartamento-precio-m2-ciudades-colombia-2026`](https://huggingface.co/datasets/aptologia/casa-vs-apartamento-precio-m2-ciudades-colombia-2026)
(precio por m² de casas y apartamentos en ciudades de Colombia, 2026).

**Flujo:** clase de carga → DataFrame → transformaciones → clase de resumen → archivo `.txt`

## Ejecución

### Automática (GitHub Actions)
Cada vez que se sube un cambio a la carpeta `EA1`, el workflow `.github/workflows/ejecutar-ea1.yml`
instala las dependencias, ejecuta el notebook con Python 3.12 y guarda en el repositorio el notebook con
sus resultados y el archivo `.txt`. También se puede lanzar a mano desde la pestaña **Actions → Ejecutar EA1 → Run workflow**.

### Local
```bash
git clone https://github.com/kevinsepulveda-iud/AD_2026Q4.git
cd AD_2026Q4
python -m pip install -r requirements.txt
cd EA1
jupyter notebook EA1_carga_y_resumen.ipynb
```
Ejecutar las celdas en orden (Python 3.12).

## Uso de inteligencia artificial

De acuerdo con el reglamento estudiantil, declaro que en este trabajo usé **Claude (Anthropic)** como asistente de
inteligencia artificial para:

- Proponer la estructura de las clases y escribir una primera versión del código.
- Revisar errores y probar el flujo completo.
- Redactar la documentación (README y explicaciones de los notebooks).
- Configurar la ejecución automática con GitHub Actions.

Revisé, ejecuté y entiendo todo el código entregado. La elección de los datasets, las transformaciones aplicadas
y los resultados los verifiqué antes de hacer la entrega.
