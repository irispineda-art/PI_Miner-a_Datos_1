# 📊 Proyecto Integrador: Minería de Datos I

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red)
![Status](https://img.shields.io/badge/Estado-Completado-brightgreen)

## 📌 Información General

* **Institución:** Instituto Tecnológico de Santiago del Estero (ITSE)
* **Materia:** Minería de Datos I (Turno Mañana)
* **Entrega:** Julio 2026
* **Integrantes:** 
  * Iris Macarena Pineda 
  * Santiago Verón
* **Sede Sumampa**

Este proyecto desarrolla un **pipeline integral e interactivo de Ciencia de Datos** aplicado a la auditoría de usuarios de una plataforma de streaming. Transforma un conjunto de datos crudos (*raw*) con inconsistencias, valores nulos y registros duplicados en conocimientos accionables mediante inspección, limpieza estadística, análisis exploratorio y reducción de dimensionalidad con PCA.

---

## 🎯 Objetivos

- **General:** Diseñar y desplegar un pipeline de procesamiento y análisis de datos completamente reproducible que transforme datos crudos en *insights* estratégicos para el negocio de streaming.
- **Técnicos:**
  - Auditar la calidad de los registros iniciales y corregir distorsiones.
  - Aplicar reducción de dimensionalidad (PCA) para eliminar la redundancia de información.
  - Exponer todo el flujo de trabajo a través de un panel web interactivo para facilitar la toma de decisiones.

---

## 📂 Estructura del Repositorio

```text
PI_Mineria_Datos_1/
│
├── README.md                   <-- Documentación principal del proyecto
├── requirements.txt            <-- Dependencias y librerías del entorno
│
├── data/
│   ├── raw/                    <-- Dataset original ('streaming_users.json')
│   └── processed/              <-- Dataset limpio ('streaming_users_clean.csv')
│
├── notebooks/
│   ├── 01_inspeccion_inicial.ipynb
│   ├── 02_calidad_y_limpieza.ipynb
│   ├── 03_eda.ipynb
│   ├── 04_pca.ipynb
│   └── 05_conclusiones.ipynb
│
├── app/
│   ├── Home.py                 <-- Página principal del Dashboard
│   └── pages/
│       ├── 01_Dataset.py       <-- Reporte de calidad y logs
│       ├── 02_EDA.py           <-- Análisis exploratorio interactivo
│       ├── 03_PCA.py           <-- Proyección espacial y varianza
│       └── 04_Conclusiones.py  <-- Hallazgos y próximos pasos
│
├── reports/
│   └── informe_final.pdf       <-- Documentación formal en PDF
│
└── logs/
    └── pipeline_log.csv        <-- Registro automatizado de transformaciones
## Preparación y calidad de datos

Eliminación de registros duplicados por ID. Homogeneización de categorías de texto. Corrección de valores lógicamente imposibles. Winsorización robusta por IQR para acotar outliers en minutos y tickets. Imputación diferenciada de nulos según el mecanismo de falta.

## Resumen del análisis exploratorio

La fase del EDA automatiza de forma visual las siguientes tareas estadísticas:
* Gráficos univariados para analizar la distribución y frecuencias de cada variable
* Gráficos bivariados para evaluar relaciones cruzadas entre los usuarios.
* Matrices de correlación multivariada para identificar redundancias de información.

## Reducción de dimensionalidad

El proceso matemático para remover el acoplamiento de los datos consiste en:
1. Selección de variables numéricas correlacionadas.
2. Escalado y estandarización de los datos.
3. Aplicación de PCA para transformar las variables en componentes ortogonales.
4. Exportación de las nuevas coordenadas bidimensionales de los usuarios.

## Visualización interactiva

La aplicación web streamlit cloud se organiza en las siguientes pantallas navegables:
* **Home:** Presentación del equipo, contexto del pipeline y enlace a Github.
* **Dataset:** Reporte de calidad del proceso y logs de las transformaciones.
* **EDA:** Gráfico de distribución de histogramas interactivos con selectores.
* **PCA:** Visualización de la varianza explicada y la proyección espacial de la muestra.

## Cómo ejecutar localmente

1. Clonar repositorio e instalar dependencias.
2. Correr la aplicación interactiva.

## Conclusiones

* Se consolidó un pipeline automatizado reproducible y auditado por logs.
* El tratamiento robusto garantizó un 98.4% de retención estructural sin sesgar la muestra.
* El espacio ortogonal de PCA eliminó las redundancias dejándolo óptimo para clustering.
* Se documentaron las limitaciones del dataset y la necesidad de sumar variables cualitativas a futuro.
