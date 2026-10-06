import streamlit as st
import pandas as pd
import os

# Configuración de la página
st.set_page_config(page_title="Dataset - PI Minería", page_icon="🗃️", layout="wide")

st.title("🗃️ Análisis y Estructura del Dataset")
st.markdown("En esta sección se presenta el estado del conjunto de datos limpio y procesado tras el pipeline de ingeniería de datos.")

st.markdown("---")

# 1. DESCRIPCIÓN GENERAL (Modifica el texto según tu temática real)
st.subheader("📝 1. Descripción General")
st.write(
    "El dataset seleccionado para este proyecto final comprende los registros procesados para el análisis de "
    "[Inserta aquí de qué es tu dataset, ej: ventas de autos, comportamiento de usuarios, etc.]. "
    "Esta información es la base utilizada para los análisis exploratorios avanzados y el modelo de reducción "
    "de dimensionalidad (PCA)."
)

# Ruta al archivo limpio
RUTA_CSV = os.path.join("data", "processed", "streaming_users_clean.csv")

try:
    # Carga eficiente de los datos limpios
    df = pd.read_csv(RUTA_CSV)

    # 2. VISTA PREVIA SIMPLE
    st.subheader("👀 2. Vista Previa de los Datos Procesados")
    filas_mostrar = st.slider("Selecciona la cantidad de filas a visualizar en la tabla:", min_value=5, max_value=50, value=10)
    st.dataframe(df.head(filas_mostrar), use_container_width=True)

    st.markdown("---")

    # 3. RESUMEN BREVE DE CALIDAD
    st.subheader("📊 3. Resumen Estructural y Calidad de Datos")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(label="Total de Registros (Filas)", value=df.shape[0])
    with col2:
        st.metric(label="Total de Variables (Columnas)", value=df.shape[1])
    with col3:
        nulos_totales = df.isnull().sum().sum()
        st.metric(label="Valores Nulos Remanentes", value=nulos_totales, delta="Pipeline Limpio" if nulos_totales == 0 else "Nulos detectados")

    # Mostrar tipos de datos de forma compacta
    st.markdown("**Estructura de tipos de datos por columna:**")
    tipos_df = pd.DataFrame(df.dtypes, columns=["Tipo"]).astype(str).T
    st.dataframe(tipos_df, use_container_width=True)

except FileNotFoundError:
    st.error(f"❌ No se encontró el archivo en la ruta: `{RUTA_CSV}`")
    st.info("💡 Por favor, descarga tu CSV limpio de Colab, renombralo a `datos_procesados.csv` y guardalo dentro de la carpeta `data/processed/`.")

st.markdown("---")

# 4. MENCIÓN BREVE DE LAS TRANSFORMACIONES PRINCIPALES (Obligatorio por consigna)
st.subheader("⚙️ 4. Transformaciones Principales Aplicadas (Pipeline ETL)")
st.markdown(
    """
    De acuerdo con lo registrado en nuestro archivo de control `logs/pipeline_log.csv`, se realizaron las siguientes transformaciones críticas:
    * **Limpieza Inicial:** Tratamiento y remoción de registros duplicados en el identificador único.
    * **Imputación/Filtrado:** Manejo de valores faltantes mediante descarte estratégico o imputación estadística (media/mediana) según la distribución de la variable.
    * **Ajuste de Tipos:** Conversión y normalización de formatos (fechas, variables categóricas y tipos numéricos).
    * **Tratamiento de Outliers:** Identificación y truncado/eliminación de valores atípicos mediante el método del rango intercuartílico (IQR) para evitar distorsiones en el PCA.
    """
)

# Pie de página con enlace obligatorio al repositorio
st.markdown("---")
st.caption("🔗 [Volver al Repositorio de GitHub](https://github.com/SantiagoVeron-HLW/PI_Mineria_De_Datos_I/tree/main")
