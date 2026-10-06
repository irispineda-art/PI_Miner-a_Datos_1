import streamlit as st

st.set_page_config(page_title="Conclusiones", layout="wide")

st.title("🏁 Conclusiones, Limitaciones y Próximos Pasos")
st.markdown("---")

st.markdown("### 📌 Hallazgos Principales")
st.write(
    "El procesamiento del archivo crudo permitio corregir un volumen critico de registros duplicados, valores faltantes e inconsistencias " \
    "categoricas imposibles, consolidando un dataset depurado y apto para la toma de decisiones estrategicas"
)

st.markdown("---")

col_c1, col_c2 = st.columns(2)

with col_c1:
    st.markdown("### ⚠️ Limitaciones Identificadas")
    st.warning("""
    El alcance de las conclusiones se encuentra condicionado por la información disponible y por las decisiones "
    "documentadas durante el proceso. En particular, al no contar con variables temporales longitudinales "
    "o historial de facturación de meses previos, el análisis de comportamiento queda restringido a una captura estática de uso mensual.
    """)

with col_c2:
    st.markdown("### 🚀 Próximos Pasos y Mejoras Futuras")
    st.success("""
    Una mejora futura podría consistir en incorporar información adicional que permita ampliar el alcance del análisis. "
    Se sugeriría integrar registros de errores específicos de la interfaz web para cruzar las fallas técnicas "
    con los reclamos presentados por los usuarios.
    """)
