# 📊 Proyecto Integrador: Minería de Datos I

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Cloud-red)
![Estado](https://img.shields.io/badge/Estado-Completado-brightgreen)

> Pipeline reproducible de Ciencia de Datos para la auditoría de usuarios de una plataforma de streaming: inspección, limpieza, análisis exploratorio y reducción dimensional con PCA, expuesto en una app web interactiva.

🔗 **Demo en vivo:** [Ver aplicación en Streamlit Cloud](https://yzbu2kwpecop22hhwf4nd7.streamlit.app/)

---

## 📌 Información General

| | |
|---|---|
| **Institución** | Instituto Tecnológico de Santiago del Estero (ITSE) |
| **Materia** | Minería de Datos I (Turno Mañana) |
| **Entrega** | Julio 2026 |
| **Integrantes** | Iris Pineda Macarena · Santiago Verón (Sumampa) |

A partir de un conjunto de datos crudos con inconsistencias, nulos y duplicados, el proyecto automatiza la inspección, la limpieza estadística, el análisis exploratorio y la reducción dimensional mediante PCA para eliminar redundancias. Todo el proceso se expone de forma interactiva para facilitar la visualización de hallazgos y la toma de decisiones.

---

## 🎯 Objetivos

**General**

Diseñar y desplegar un pipeline de procesamiento y análisis de datos completamente reproducible, que transforme datos crudos en conocimiento accionable para el negocio del streaming.

**Técnicos**

- Auditar la calidad de los registros iniciales.
- Corregir distorsiones mediante técnicas de limpieza.
- Aplicar reducción de dimensionalidad (PCA) para eliminar la redundancia de información.
- Exponer todo el flujo de trabajo a través de un panel web interactivo.

---

## 🗃️ Conjunto de Datos

| Archivo | Ubicación | Descripción |
|---|---|---|
| `streaming_users.json` | `data/raw/` | Dataset original con métricas de uso, datos demográficos, identificadores, transacciones y planes de suscripción. |
| `streaming_users_clean.csv` | `data/processed/` | Dataset resultante tras la limpieza y el procesamiento. |

---

## 📁 Estructura del Repositorio

```text
PI_Mineria_Datos_1/
│
├── README.md                      <- Documentación principal
├── requirements.txt               <- Dependencias del entorno
│
├── data/
│   ├── raw/                       <- Dataset original (streaming_users.json)
│   └── processed/                 <- Dataset limpio (streaming_users_clean.csv)
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
```

---

## 🛠️ Pipeline de Procesamiento

### 1. Preparación y calidad de datos

- **Duplicados:** eliminación de registros repetidos por ID.
- **Normalización:** homogeneización de categorías de texto.
- **Lógica de negocio:** corrección de valores lógicamente imposibles.
- **Outliers:** winsorización robusta por IQR para acotar valores extremos en minutos de uso y tickets.
- **Imputación:** tratamiento diferenciado de nulos según el mecanismo de falta.

### 2. Análisis Exploratorio (EDA)

- **Univariado:** distribución y frecuencias de cada variable.
- **Bivariado:** relaciones cruzadas entre perfiles de usuarios.
- **Multivariado:** matrices de correlación para identificar redundancias.

### 3. Reducción de dimensionalidad (PCA)

1. Selección de variables numéricas correlacionadas.
2. Escalado y estandarización de los datos.
3. Aplicación de PCA para obtener componentes ortogonales.
4. Exportación de las coordenadas bidimensionales de los usuarios.

---

## 🖥️ Aplicación Interactiva

La app desplegada en Streamlit Cloud se organiza en cuatro pantallas:

| Página | Contenido |
|---|---|
| 🏠 **Home** | Presentación del equipo, contexto del pipeline y enlace a GitHub. |
| 🗂️ **Dataset** | Reporte de calidad y logs de las transformaciones. |
| 📈 **EDA** | Histogramas interactivos con selectores. |
| 🔵 **PCA** | Varianza explicada y proyección espacial de la muestra. |

---

## 🚀 Cómo ejecutar localmente

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU-USUARIO/PI_Mineria_Datos_1.git
cd PI_Mineria_Datos_1

# 2. Instalar dependencias
pip install -r requirements.txt

# 3. Correr la aplicación
streamlit run app/Home.py
```

---

## ✅ Conclusiones

- Se consolidó un pipeline automatizado, reproducible y auditado mediante logs.
- El tratamiento robusto garantizó una **retención estructural del 98.4 %** sin sesgar la muestra.
- El espacio ortogonal de PCA eliminó las redundancias, dejando los datos en condiciones óptimas para clustering.
- Se documentaron las limitaciones del dataset y la necesidad de incorporar variables cualitativas a futuro.

---

## 👥 Autores

- **Iris Pineda Macarena**
- **Santiago Verón (Sumampa)**
