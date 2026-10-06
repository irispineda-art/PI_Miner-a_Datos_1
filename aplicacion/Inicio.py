import streamlit as st

# Configuración global de la página
st.set_page_config(
    page_title="PI Minería de Datos",
    page_icon="🏠",
    layout="wide"
)

# Título Principal
st.title("🚀 Proyecto Integrador: Minería de Datos I")
st.subheader("Aplicación Interactiva de Visualización y Análisis")

st.markdown("---")

# Distribución en columnas para la información del grupo
col1, col2 = st.columns(2)

with col1:
    st.markdown("### 👥 Integrantes")
    # TODO: Reemplaza con los nombres reales de tu grupo
    st.markdown("- **Pineda, Iris Macarena**")
    st.markdown("- **Veron, Santiago**")

with col2:
    st.markdown("### 📋 Información Académica")
    st.markdown("**Comisión:** Mineria de Datos. Turno mañana")
    st.markdown("**Fecha:** Julio 2026")
    st.markdown("**Institución:** Instituto tecnologico de santiago")

st.markdown("---")

# Contexto Breve
st.markdown("### 📝 Contexto del Proyecto")
st.write(
    "Esta aplicación web interactiva presenta los resultados del pipeline de minería de datos, "
    "abarcando desde la inspección inicial, limpieza, análisis exploratorio (EDA) "
    "hasta la reducción de dimensionalidad mediante PCA. El objetivo es proporcionar una interfaz "
    "accesible para público general y tomadores de decisiones."
)

st.markdown("---")

# Enlace obligatorio a GitHub usando el componente nativo o markdown
st.markdown("### 🔗 Repositorio del Proyecto")
st.link_button("Ver Código Fuente en GitHub", "https://github.com/SantiagoVeron-HLW/PI_Mineria_De_Datos_I/")
