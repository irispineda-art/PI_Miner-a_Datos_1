# 📊 Proyecto Integrador: Minería de Datos I
## Python + Streamlit Status

---

## 📌 Información General

**Institución:** Instituto Tecnológico de Santiago del Estero (ITSE)  
**Materia:** Minería de Datos I (Turno Mañana)  
**Entrega:** Julio 2026  
**Integrantes:**  
- Iris Macarena Pineda
- Santiago Verón

**Sede:** Sumampa

Este proyecto desarrolla un pipeline integral e interactivo de Ciencia de Datos aplicado a la auditoría de usuarios de una plataforma de streaming.

El proceso transforma un conjunto de datos crudos (`raw`) que contiene inconsistencias, valores nulos, registros duplicados y valores atípicos en información limpia y estructurada, permitiendo posteriormente realizar análisis exploratorio y reducción de dimensionalidad mediante PCA.

El flujo completo se encuentra documentado mediante notebooks y registros de transformación, y sus resultados son expuestos mediante una aplicación web interactiva desarrollada con Streamlit.

---

## 🎯 Objetivos

### Objetivo General

Diseñar y desplegar un pipeline de procesamiento y análisis de datos completamente reproducible que permita transformar datos crudos de usuarios de una plataforma de streaming en información útil para la generación de insights y la toma de decisiones.

### Objetivos Técnicos

- 🔍 Auditar la calidad de los registros iniciales.
- 🧹 Detectar y corregir inconsistencias en los datos.
- 📊 Realizar un análisis exploratorio de las variables.
- 🔗 Identificar relaciones y posibles redundancias entre variables.
- 🧮 Aplicar reducción de dimensionalidad mediante PCA.
- 💻 Exponer los resultados mediante una aplicación web interactiva.
- 📝 Registrar las transformaciones realizadas mediante logs.
- 🔄 Mantener un pipeline reproducible y documentado.

---

## 📂 Estructura del Repositorio

```text
PI_Mineria_Datos_1/
│
├── README.md                   <-- Documentación principal del proyecto
├── requirements.txt            <-- Dependencias y librerías del entorno
│
├── data/
│   ├── raw/                    <-- Dataset original
│   │   └── streaming_users.json
│   │
│   └── processed/              <-- Dataset procesado
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
│   ├── Home.py                 <-- Página principal del Dashboard
│   │
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
