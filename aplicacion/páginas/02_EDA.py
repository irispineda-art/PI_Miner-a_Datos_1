import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import os

# Configuración de la página
st.set_page_config(page_title="EDA - PI Minería", page_icon="📊", layout="wide")

st.title("📊 Análisis Exploratorio de Datos (EDA)")
st.markdown("Resultados analíticos del comportamiento de la base de usuarios activos.")

st.markdown("---")

RUTA_CSV = os.path.join("data", "processed", "streaming_users_clean.csv")

try:
    df_eda = pd.read_csv(RUTA_CSV)

    # =========================================================================
    # 1. VISUALIZACIONES UNIVARIADAS (2 exactas)
    # =========================================================================
    st.header("📈 1. Análisis Univariado")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Gráfico 1: Distribución Demográfica")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(
            data=df_eda,
            x='age',
            kde=True,
            color='#14365D',
            alpha=0.75,
            bins=20,
            edgecolor='white',
            linewidth=0.8,
            ax=ax
        )
        ax.set_title('Distribución Demográfica: Edad de los Usuarios Activos', fontsize=12, fontweight='bold', pad=15)
        ax.set_xlabel('Edad del Usuario (Años)', fontsize=10)
        ax.set_ylabel('Frecuencia (Usuarios)', fontsize=10)
        ax.xaxis.set_major_locator(ticker.MultipleLocator(5))
        sns.despine(left=True, bottom=True)
        st.pyplot(fig)
        
        st.markdown("**Interpretación:**")
        st.write(
            "La distribución de los usuarios activos se concentra principalmente en un rango de edad madura, "
            "desde los 18 años hasta los 65 años, con una clara asimetría hacia la derecha. El rasgo más notorio "
            "es la acumulación atípica en el intervalo de 30-35 años, debido a la imputación por medianas acumuladas "
            "según el perfil de consumo (género favorito y plan), preservando la coherencia demográfica del negocio[cite: 1]."
        )

    with col2:
        st.subheader("Gráfico 2: Volumen por Nivel de Suscripción")
        fig, ax = plt.subplots(figsize=(10, 6))
        order_plans = df_eda['subscription_plan'].value_counts().index
        sns.countplot(
            data=df_eda,
            x='subscription_plan',
            order=order_plans,
            palette=["#1A365D", "#2B6CB0", "#4FD1C5"],
            alpha=0.9,
            width=0.35,
            ax=ax
        )
        for p in ax.patches:
            ax.annotate(f"{int(p.get_height()):,}", (p.get_x() + p.get_width() / 2., p.get_height() + 50),
                        ha='center', va='center', fontsize=10, fontweight='bold', color='#4A5568')
        ax.set_title('Volumen de Clientes Activos por Nivel de Suscripción', fontsize=12, fontweight='bold', pad=15)
        ax.set_xlabel('Plan de Suscripción', fontsize=10)
        ax.set_ylabel('Cantidad de Usuarios', fontsize=10)
        sns.despine(left=True, bottom=True)
        st.pyplot(fig)
        
        st.markdown("**Interpretación:**")
        st.write(
            "El volumen presenta una distribución escalonada inversamente proporcional al costo del servicio. "
            "El plan básico lidera ampliamente con 3.607 usuarios, seguido por el Estándar con 2.833, "
            "mientras el Premium concentra el segmento más exclusivo con 1.592 usuarios[cite: 1]."
        )

    st.markdown("---")

    # =========================================================================
    # 2. VISUALIZACIONES BIVARIADAS (2 exactas)
    # =========================================================================
    st.header("🔀 2. Análisis Bivariado")
    col3, col4 = st.columns(2)

    with col3:
        st.subheader("Gráfico 3: Consumo Mensual por Plan")
        fig, ax = plt.subplots(figsize=(10, 6))
        orden_planes = ['Básico', 'Estándar', 'Premium']
        sns.boxplot(
            data=df_eda,
            x='subscription_plan',
            y='monthly_watch_time_mins',
            order=[p for p in orden_planes if p in df_eda['subscription_plan'].unique()],
            palette="Blues",
            width=0.4,
            linewidth=1.2,
            fliersize=4,
            ax=ax
        )
        ax.set_title('Consumo Mensual por Segmento de Plan', fontsize=12, fontweight='bold', pad=15)
        ax.set_xlabel('Plan de Suscripción', fontsize=10)
        ax.set_ylabel('Minutos de Reproducción por Mes', fontsize=10)
        sns.despine(left=True, bottom=True)
        st.pyplot(fig)
        
        st.markdown("**Interpretación:**")
        st.write(
            "Existe una relación directa entre el nivel de suscripción y el tiempo de permanencia: "
            "a mayor jerarquía comercial, aumentan los minutos mensuales. El plan básico promedia los 600 minutos, "
            "el estándar 950 y el premium supera los 1.200 minutos, confirmando que el plan es un fuerte predictor de consumo[cite: 1]."
        )

    with col4:
        st.subheader("Gráfico 4: Preferencia de Contenido por Región")
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.countplot(
            data=df_eda,
            x='country',
            hue='favorite_genre',
            palette="Blues",
            alpha=0.9,
            order=sorted(df_eda['country'].unique()),
            edgecolor='#b0b0b0',
            linewidth=0.5,
            ax=ax
        )
        ax.set_title('Análisis de Preferencia de Contenido por Región Geográfica', fontsize=12, fontweight='bold', pad=15)
        ax.set_xlabel('País de Residencia', fontsize=10)
        ax.set_ylabel('Cantidad de Usuarios', fontsize=10)
        ax.legend(title='Género Favorito', title_fontsize='10', loc='upper left', bbox_to_anchor=(1, 1), frameon=False)
        sns.despine(left=True, bottom=True)
        st.pyplot(fig)
        
        st.markdown("**Interpretación:**")
        st.write(
            "Se observa una notable homogeneidad en el volumen de usuarios por país, mostrando un mercado estable. "
            "No obstante, se detectan microtendencias específicas, como el interés por el género Crimen en Chile "
            " o la Comedia en Brasil y Colombia, útiles para dirigir estrategias de marketing enfocadas[cite: 1]."
        )

    st.markdown("---")

    # =========================================================================
    # 3. VISUALIZACIÓN MULTIVARIADA (1 exacta)
    # =========================================================================
    st.header("🌐 3. Análisis Multivariado")
    
    st.subheader("Gráfico 5: Mapeo de Edad y Consumo por Plan")
    PLATFORM_PALETTE = {"Básico": "#286CB0", "Estándar": "#4FD1C5", "Premium": "#ED64A6"}
    
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.scatterplot(
        data=df_eda,
        x='age',
        y='monthly_watch_time_mins',
        hue='subscription_plan',
        palette=PLATFORM_PALETTE,
        alpha=0.6,
        s=45,
        edgecolor='none',
        ax=ax
    )
    ax.set_title('Mapeo de Comportamiento: Relación de Edad y Consumo por Plan de Suscripción', fontsize=14, fontweight='bold', pad=15)
    ax.set_xlabel('Edad del Usuario (Años)', fontsize=10)
    ax.set_ylabel('Minutos de Reproducción Mensual', fontsize=10)
    ax.xaxis.set_major_locator(ticker.MultipleLocator(10))
    ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))
    ax.legend(title='Plan de Suscripción', title_fontsize='11', loc='upper right', frameon=True, facecolor='white', edgecolor='#e2e8f0')
    sns.despine(left=True, bottom=True)
    st.pyplot(fig)
    
    st.markdown("**Interpretación:**")
    st.write(
        "El mapa de dispersión multivariado segmenta claramente las franjas de consumo según el plan adquirido "
        "sin importar la edad del usuario, evidenciando franjas horizontales bien delimitadas. Permite visualizar "
        "fácilmente a los usuarios atípicos (outliers) de consumos altos en planes económicos para campañas de upgrade[cite: 1]."
    )

except FileNotFoundError:
    st.error("❌ No se encontró el archivo 'datos_procesados.csv' en 'data/processed/'.")
