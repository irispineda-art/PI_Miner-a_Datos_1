import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os

# Configuración de la página
st.set_page_config(page_title="PCA - PI Minería", page_icon="🧬", layout="wide")

st.title("🧬 Reducción de Dimensionalidad (PCA)")
st.markdown("Análisis de Componentes Principales ejecutado sobre las variables métricas del dataset procesado.")

st.markdown("---")

# Intentamos cargar el dataset limpio del proyecto
RUTA_CSV = os.path.join("data", "processed", "streaming_users_clean.csv")

try:
    df = pd.read_csv(RUTA_CSV)
    
    # Variables exactas de tu notebook
    columnas_num = ['age', 'monthly_watch_time_mins']
    
    # Validar que existan las columnas en el CSV procesado
    if all(col in df.columns for col in columnas_num):
        
        st.subheader("📋 1. Variables Seleccionadas y Escalamiento")
        st.write(
            f"De acuerdo con el pipeline del notebook, se seleccionaron las variables cuantitativas: "
            f"`{', '.join(columnas_num)}`."
        )
        
        # Preparación y Estandarización idéntica a tu StandardScaler()
        X = df[columnas_num].copy().dropna()
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(X)
        
        # Ajustar el modelo PCA con 2 componentes
        pca = PCA(n_components=2)
        X_pca = pca.fit_transform(X_scaled)
        
        # Extraer varianzas
        varianza_explicada = pca.explained_variance_ratio_
        varianza_acumulada = np.cumsum(varianza_explicada)
        
        # Mostrar métricas solicitadas por la consigna
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.metric(label="Varianza Explicada PC1", value=f"{varianza_explicada[0]*100:.2f} %")
        with col_m2:
            st.metric(label="Varianza Explicada PC2", value=f"{varianza_explicada[1]*100:.2f} %")
            
        st.success(f"✅ Varianza Acumulada Total: {(varianza_acumulada[1]*100):.2f}% (Se retiene el 100% de la variabilidad sin pérdida de información).")

        # Mostrar Tabla de Loadings técnica
        st.markdown("**Tabla de Loadings (Contribución a PC1 y PC2):**")
        loadings = pca.components_
        df_loadings = pd.DataFrame(loadings.T, columns=['PC1', 'PC2'], index=columnas_num)
        st.dataframe(df_loadings.round(3), use_container_width=True)

        st.markdown("---")
        st.header("📊 2. Visualizaciones Oficiales (Máximo 2)")
        
        col1, col2 = st.columns(2)
        
        # ---------------------------------------------------------------------
        # GRÁFICO 1: VARIANZA EXPLICADA POR COMPONENTE
        # ---------------------------------------------------------------------
        with col1:
            st.subheader("1. Varianza Explicada por Componente (PCA)")
            
            fig1, ax1 = plt.subplots(figsize=(6, 4))
            
            # Barras individuales
            ax1.bar(range(1, 3), varianza_explicada, alpha=0.6, align='center', 
                    label='Varianza individual', color='lightblue')
            # Línea acumulada
            ax1.plot(range(1, 3), varianza_acumulada, marker='o', 
                     label='Varianza acumulada', color='darkblue')
            
            ax1.set_ylabel('Porcentaje de Varianza Explicada')
            ax1.set_xlabel('Componentes Principales')
            ax1.set_xticks([1, 2])
            ax1.set_xticklabels(['PC1', 'PC2'])
            ax1.set_ylim(0, 1.1)
            ax1.legend(loc='best')
            ax1.grid(axis='y', linestyle='--', alpha=0.7)
            
            st.pyplot(fig1)
            
            st.markdown("**Interpretación:**")
            st.caption(
                "Debido a la naturaleza bidimensional del análisis, se puede observar una distribución equitativa de la variabilidad entre ambos "
                "componentes. El primer componente (PC1) captura el 50.20% de la varianza total del sistema, mientras que el segundo componente "
                "(PC2) el 49.80%. La trayectoria de la línea azul ilustra la retención de la información a medida que se agregan dimensiones."
            )

        # ---------------------------------------------------------------------
        # GRÁFICO 2: PROYECCIÓN DE USUARIOS (SCATTER PLOT)
        # ---------------------------------------------------------------------
        with col2:
            st.subheader("2. Proyección de Usuarios en el Espacio PCA")
            
            fig2, ax2 = plt.subplots(figsize=(6, 4))
            
            # Scatter de usuarios idéntico al de tu notebook
            ax2.scatter(X_pca[:, 0], X_pca[:, 1], alpha=0.6, color='purple', edgecolors='w', s=40)
            
            # Ejes de simetría en 0
            ax2.axhline(0, color='black', linestyle='--', linewidth=0.8)
            ax2.axvline(0, color='black', linestyle='--', linewidth=0.8)
            
            ax2.set_xlabel('Componentes Principal 1 (PC1)')
            ax2.set_ylabel('Componentes Principal 2 (PC2)')
            ax2.grid(True, linestyle=':', alpha=0.6)
            
            st.pyplot(fig2)
            
            st.markdown("**Interpretación:**")
            st.caption(
                "Este gráfico proyecta los usuarios sobre el nuevo sistema de ejes ortogonales y no correlacionales definidos por el modelo de PCA. "
                "El eje horizontal (PC1) modula el comportamiento de usuarios maduros estables y con alta retención en la plataforma. "
                "El eje vertical (PC2) discrimina los comportamientos atípicos y el 'engagement agresivo' característico de segmentos de menor edad."
            )

    else:
        st.error(f"❌ El archivo no contiene las columnas requeridas: {columnas_num}. Verifica tu pipeline.")

except FileNotFoundError:
    st.error("❌ No se encontró el archivo `datos_procesados.csv` en la carpeta `data/processed/`.")

st.markdown("### 🔗 Repositorio del Proyecto")
st.link_button("Ver Código Fuente en GitHub", "https://github.com/SantiagoVeron-HLW/PI_Mineria_De_Datos_I/")
