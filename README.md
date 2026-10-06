📊 Proyecto Integrador: Minería de Datos I
🖥️ Python + Streamlit — Pipeline de Auditoría y Análisis de Usuarios
📌 Información General
	
Institución	Instituto Tecnológico de Santiago del Estero (ITSE)
Materia	Minería de Datos I — Turno Mañana
Entrega	Julio 2026
Sede	Sumampa
Integrantes	Iris Macarena Pineda · Santiago Verón
📖 Descripción del Proyecto

Este proyecto desarrolla un pipeline integral, reproducible e interactivo de Ciencia de Datos, aplicado a la auditoría y análisis de usuarios de una plataforma de streaming.

El proceso parte de un conjunto de datos raw que contiene inconsistencias, valores nulos, registros duplicados y valores potencialmente atípicos. A partir de diferentes técnicas de inspección, limpieza, análisis exploratorio y reducción de dimensionalidad, los datos son transformados en información útil para la generación de insights estratégicos.

Todo el flujo de trabajo se encuentra documentado mediante notebooks y registros de procesamiento, y posteriormente se expone a través de una aplicación web desarrollada con Streamlit, permitiendo explorar los resultados de manera visual e interactiva.

🎯 Objetivos
Objetivo General

Diseñar y desplegar un pipeline de procesamiento y análisis de datos completamente reproducible, capaz de transformar datos crudos de usuarios de una plataforma de streaming en información limpia, analizada y útil para la toma de decisiones.

Objetivos Técnicos

🔍 Auditar la calidad de los registros iniciales.

🧹 Detectar y corregir inconsistencias en los datos.

📊 Analizar estadísticamente las principales variables del dataset.

📈 Identificar relaciones y redundancias entre variables.

🧮 Aplicar técnicas de reducción de dimensionalidad mediante PCA.

💻 Desarrollar un dashboard interactivo utilizando Streamlit.

📝 Registrar las transformaciones realizadas mediante logs para garantizar la trazabilidad.

🔄 Mantener un flujo de trabajo reproducible y documentado.

📂 Estructura del Repositorio
PI_Mineria_Datos_1/
│
├── README.md
├── requirements.txt
│
├── data/
│   ├── raw/
│   │   └── streaming_users.json
│   │
│   └── processed/
│       └── streaming_users_clean.csv
│
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
│
├── app/
│   ├── Home.py
│   │
│   └── pages/
│       ├── 01_Dataset.py
│       ├── 02_EDA.py
│       ├── 03_PCA.py
│       └── 04_Conclusiones.py
│
├── reports/
│   └── informe_final.pdf
│
└── logs/
    └── pipeline_log.csv

🔄 Pipeline de Procesamiento

El proyecto se organiza en diferentes etapas que permiten transformar progresivamente los datos originales en información analizable.

Dataset RAW
     │
     ▼
┌──────────────────────┐
│  Inspección inicial  │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Calidad y limpieza   │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Dataset procesado    │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Análisis exploratorio│
│       (EDA)          │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Reducción dimensional│
│       (PCA)          │
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Insights y conclusiones│
└──────────┬───────────┘
           ▼
┌──────────────────────┐
│ Dashboard Streamlit  │
└──────────────────────┘

🧹 Preparación y Calidad de los Datos

La etapa de preparación tiene como objetivo garantizar que el dataset utilizado en las etapas posteriores presente una estructura consistente y confiable.

Se aplicaron las siguientes técnicas:

Eliminación de registros duplicados: se identificaron y eliminaron duplicados utilizando el ID del usuario como referencia.

Homogeneización de categorías: se normalizaron valores de texto para evitar categorías equivalentes representadas de diferentes maneras.

Corrección de valores lógicamente imposibles: se detectaron valores incompatibles con el dominio de las variables y se aplicaron las correcciones correspondientes.

Tratamiento de valores atípicos: se aplicó winsorización robusta mediante el criterio del IQR (Rango Intercuartílico) para limitar la influencia de valores extremos en variables como minutos y tickets.

Imputación de valores nulos: los valores faltantes fueron tratados de manera diferenciada de acuerdo con el mecanismo y naturaleza de cada variable.

Registro de transformaciones: las operaciones realizadas durante el pipeline fueron documentadas en pipeline_log.csv.

Como resultado, se obtuvo un dataset procesado preparado para las etapas de análisis exploratorio y reducción de dimensionalidad.

📊 Análisis Exploratorio de Datos — EDA

La etapa de Exploratory Data Analysis (EDA) permite comprender el comportamiento de las variables y detectar patrones relevantes dentro del conjunto de usuarios.

Se implementaron diferentes técnicas de visualización:

📌 Análisis Univariado

Permite estudiar individualmente cada variable mediante:

Histogramas.

Distribuciones de frecuencia.

Medidas estadísticas.

Análisis de valores atípicos.

🔗 Análisis Bivariado

Permite estudiar la relación entre dos variables mediante:

Gráficos de dispersión.

Comparaciones entre variables.

Análisis de tendencias.

Relaciones entre comportamiento de usuarios y métricas de consumo.

🔥 Análisis Multivariado

Se utilizaron matrices de correlación para identificar relaciones entre variables numéricas y detectar posibles redundancias de información.

Estos resultados sirven como base para la selección de variables utilizadas posteriormente en PCA.

🧮 Reducción de Dimensionalidad — PCA

Para reducir la complejidad del conjunto de datos se implementó Principal Component Analysis (PCA).

El procedimiento se desarrolló en las siguientes etapas:

Selección de variables numéricas con información relevante y posibles relaciones entre sí.

Estandarización de los datos, evitando que variables con diferentes escalas dominen el análisis.

Aplicación de PCA, transformando las variables originales en componentes principales ortogonales.

Análisis de la varianza explicada, para determinar cuánta información conserva cada componente.

Proyección bidimensional, utilizando los principales componentes para representar espacialmente a los usuarios.

Exportación de coordenadas, permitiendo utilizar posteriormente estas representaciones en tareas como clustering.

La transformación permite trabajar con un espacio de menor dimensión manteniendo la mayor cantidad posible de información relevante.

🖥️ Visualización Interactiva — Streamlit

El análisis se integra en una aplicación web desarrollada con Streamlit, organizada en diferentes pantallas.

🏠 Home

La página principal presenta:

Nombre e identidad del proyecto.

Integrantes del equipo.

Institución y materia.

Contexto del problema.

Descripción general del pipeline.

Acceso al repositorio de GitHub.

📋 Dataset

Esta sección permite consultar:

Calidad inicial de los datos.

Cantidad de registros.

Valores nulos.

Registros duplicados.

Transformaciones aplicadas.

Resultado del proceso de limpieza.

Logs del pipeline.

📊 EDA

La sección de análisis exploratorio presenta visualizaciones interactivas para analizar:

Distribuciones.

Frecuencias.

Relaciones entre variables.

Correlaciones.

Comportamiento general de los usuarios.

Los gráficos cuentan con selectores que permiten explorar diferentes variables de manera dinámica.

🧮 PCA

La sección de reducción de dimensionalidad permite visualizar:

Varianza explicada.

Importancia de los componentes.

Proyección bidimensional de los usuarios.

Distribución espacial de las observaciones.

📝 Conclusiones

La última sección reúne:

Principales hallazgos.

Resultados obtenidos.

Limitaciones del dataset.

Posibles mejoras.

Próximos pasos del proyecto.

📓 Notebooks

El desarrollo analítico se encuentra dividido en cinco notebooks para facilitar la trazabilidad del proyecto:

Notebook	Contenido
01_inspeccion_inicial.ipynb	Exploración y diagnóstico inicial del dataset
02_calidad_y_limpieza.ipynb	Tratamiento de calidad, nulos, duplicados y outliers
03_eda.ipynb	Análisis exploratorio y visualización
04_pca.ipynb	Estandarización, PCA y análisis de varianza
05_conclusiones.ipynb	Interpretación de resultados y conclusiones
📈 Resultados Principales

A partir del procesamiento realizado se obtuvieron los siguientes resultados:

Se consolidó un pipeline automatizado y reproducible.

Se implementó un sistema de registro mediante logs que permite realizar un seguimiento de las transformaciones.

El tratamiento de los datos permitió alcanzar un 98,4 % de retención estructural de la muestra.

La aplicación de PCA permitió transformar las variables seleccionadas en un espacio de componentes ortogonales.

La reducción dimensional permite disponer de una representación adecuada para futuras técnicas de segmentación y clustering.

El análisis exploratorio permitió identificar relaciones y patrones relevantes entre las variables disponibles.

⚠️ Limitaciones

Durante el desarrollo se identificaron algunas limitaciones relacionadas con la información disponible:

El dataset presenta una cantidad limitada de variables cualitativas.

Algunas variables podrían requerir información contextual adicional.

La representación mediante PCA depende de las variables numéricas seleccionadas.

Los resultados obtenidos corresponden al conjunto de datos disponible y no necesariamente representan a toda la población de usuarios de una plataforma real.

🚀 Próximos Pasos

Como posibles extensiones del proyecto se plantea:

Incorporar nuevas variables cualitativas relacionadas con los usuarios.

Incorporar técnicas de clustering sobre las coordenadas obtenidas mediante PCA.

Analizar perfiles o segmentos de usuarios.

Incorporar nuevos períodos temporales para realizar análisis evolutivos.

Implementar métricas adicionales para evaluar el comportamiento de los usuarios.

Ampliar el dashboard con nuevos filtros y visualizaciones.

Evaluar otros métodos de reducción de dimensionalidad para comparar resultados.

▶️ Cómo Ejecutar el Proyecto Localmente
1. Clonar el repositorio
git clone <URL_DEL_REPOSITORIO>
cd PI_Mineria_Datos_1

2. Crear un entorno virtual
python -m venv .venv

Windows
.venv\Scripts\activate

Linux / macOS
source .venv/bin/activate

3. Instalar las dependencias
pip install -r requirements.txt

4. Ejecutar la aplicación
streamlit run app/Home.py


Una vez iniciada, Streamlit proporcionará la dirección local para acceder al dashboard desde el navegador.

☁️ Despliegue

La aplicación puede desplegarse mediante Streamlit Community Cloud, vinculando el repositorio y configurando como archivo principal:

app/Home.py


Las dependencias necesarias para la ejecución se encuentran especificadas en:

requirements.txt

📄 Documentación

La documentación formal del proyecto se encuentra disponible en:

reports/informe_final.pdf


Además, cada etapa del análisis cuenta con su correspondiente notebook dentro del directorio:

notebooks/

👥 Equipo

Instituto Tecnológico de Santiago del Estero — ITSE

Materia: Minería de Datos I — Turno Mañana
Sede: Sumampa
Entrega: Julio 2026

Integrantes

Iris Macarena Pineda

Santiago Verón

🎓 Conclusión

El proyecto permitió integrar diferentes etapas de un proceso de Minería de Datos, desde la inspección y limpieza de información hasta el análisis exploratorio y la reducción de dimensionalidad.

La combinación de Python, análisis estadístico, PCA, notebooks y Streamlit permitió construir un flujo reproducible que no solo procesa los datos, sino que también facilita la interpretación y comunicación de los resultados.

De esta manera, el proyecto constituye una implementación integral de un pipeline de Ciencia de Datos orientado a transformar datos crudos en información útil para el análisis y la toma de decisiones.
