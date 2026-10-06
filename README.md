# 📊 Proyecto Integrador: Minería de Datos I

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red)
![Status](https://img.shields.io/badge/Estado-Completado-brightgreen)

## 📌 Información General

* **Institución:** Instituto Tecnológico de Santiago del Estero (ITSE)
* **Materia:** Minería de Datos I (Turno Mañana)
* **Entrega:** Julio 2026
* **Integrantes:** 
  * Iris Pineda Macarena
  * Santiago Verón (Sumampa)

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

## 🧹 Preparación y Calidad de Datos
La primera etapa del proyecto se enfoca en evaluar y mejorar la calidad del dataset original.

Se aplicaron diferentes técnicas de preparación y limpieza:
🗑️ Eliminación de registros duplicados: se identificaron registros repetidos utilizando el ID del usuario.

🔤 Homogeneización de categorías: se normalizaron valores de texto para evitar categorías equivalentes representadas de diferentes maneras.

⚠️ Corrección de valores lógicamente imposibles: se detectaron y corrigieron valores incompatibles con el contexto de las variables.

📉 Tratamiento de valores atípicos: se aplicó winsorización robusta mediante el método del IQR para limitar la influencia de valores extremos en variables como minutos y tickets.

🧩 Imputación de valores nulos: los valores faltantes fueron tratados de acuerdo con la naturaleza y mecanismo de ausencia de cada variable.

📝 Registro de transformaciones: todas las operaciones realizadas fueron registradas en pipeline_log.csv.

El resultado de esta etapa es un dataset limpio y estructurado que puede ser utilizado para las etapas posteriores de análisis.

