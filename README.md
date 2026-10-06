PT_Mineria_De_Datos_1
Trabajo realizado por Iris Pineda Macarena y Satiago Veron de Sumampa Proyecto Integrador: Minería de Datos I

Información General
Este trabajo práctico fue realizado para la materia “Minería de Datos I”, Turno Mañana, de la carrera del Instituto Tecnológico de Santiago del Estero (ITSE), correspondiente a la entrega de julio 2026. El proyecto cuenta con un despliegue operativo en el siguiente enlace público El trabajo consiste en el desarrollo integral de un pipeline de Ciencia de Datos aplicado a la auditoría de usuarios de una plataforma de streaming. A partir de un conjunto de datos crudos que presenta inconsistencias, nulos y duplicados, el proyecto automatiza las etapas de inspección, limpieza estadística, análisis exploratorio y reducción dimensional mediante PCA, para eliminar redundancias. Todo este proceso técnico se expone de manera interactiva a través de una interfaz web para facilitar la visualización de los hallazgos y la toma de decisiones.

Objetivos
El objetivo principal de este trabajo es diseñar y desplegar un pipeline de procesamiento y análisis de datos completamente reproducible que permita transformar datos crudos en conocimientos accionables para el negocio del streaming. Para lograrlo, la meta técnica se centra en auditar la calidad de los registros iniciales, corregir sus distorsiones mediante técnicas de limpieza y aplicar una reducción de dimensionalidad que elimina la redundancia de información, exponiendo todo el flujo de trabajo de forma interactiva para los tomadores de decisiones.

Conjunto de datos
El proyecto procesa el archivo ‘streaming_users.json’, el cual contiene métricas de uso demográficas, identificadoras, transacciones y planes de subscripción. Una vez procesado, el dataset extraído recibe el nombre de ‘streaming_users_clean.csv’, almacenado en Data/processed.

Estructura de Repositorio
PI_Mineria_Datos_1/ │ ├── README.md ├── requirements.txt │ ├── data/ │ ├── raw/ │ └── processed/ │ ├── notebooks/ │ ├── 01_inspeccion_inicial.ipynb │ ├── 02_calidad_y_limpieza.ipynb │ ├── 03_eda.ipynb │ ├── 04_pca.ipynb │ └── 05_conclusiones.ipynb │ ├── app/ │ ├── Home.py │ └── pages/ │ ├── 01_Dataset.py │ ├── 02_EDA.py │ ├── 03_PCA.py │ └── 04_Conclusiones.py
│ ├── reports/ │ └── informe_final.pdf │ └── logs/ └── pipeline_log.csv

Preparación y calidad de datos:
Eliminación de registros duplicados por ID. Homogeneización de categorías de texto. Corrección de valores lógicamente imposibles. Winsorización robusta por IQR para acotar outliers en minutos y tickets. Imputación diferenciada de nulos según el mecanismo de falta.

Resumen del análisis exploratorio
La fase del EDA automatiza de forma visual las siguientes tareas estadísticas: Gráficos univariados para analizar la distribución y frecuencias de cada variable Gráficos bivariados para evaluar relaciones cruzadas entre los usuarios. Matrices de correlación multivariada para identificar redundancias de información.

Reducción de dimensionalidad
El proceso matemático para remover el acoplamiento de los datos consiste en: Selección de variables numéricas correlacionadas. Escalado y estandarización de los datos. Aplicación de PCA para transformar las variables en componentes ortogonales. Exportación de las nuevas coordenadas bidimensionales de los usuarios.

Visualización interactiva
La aplicación web streamlit cloud se organiza en las siguientes pantallas navegables:

Home: Presentación del equipo, contexto del pipeline y enlace a Github. Dataset: Reporte de calidad del proceso y logs de las transformaciones. EDA: Gráfico de distribución de histogramas interactivos con selectores. PCA: Visualización de la varianza explicada y la proyección espacial de la muestra.

Cómo ejecutar localmente
Clonar repositorio e instalar dependencias Correr la aplicación interactiva

Conclusiones
Se consolidó un pipeline automatizado reproducible y auditado por logs
El tratamiento robusto garantizó un 98.4% de retención estructural sin sesgar la muestra. El espacio ortogonal de PCA eliminó las redundancias dejándolo óptimo para clustering. Se documentaron las limitaciones del dataset y la necesidad de sumar variables cualitativas a futuro.
