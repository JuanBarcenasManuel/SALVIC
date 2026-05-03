import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SALVIC C.A. | Catálogo 2026",
    page_icon="📦",
    layout="wide"
)

# --- 2. ESTILO MINIMALISTA PREMIUM ---
st.markdown("""
    <style>
    /* Fondo general ultra limpio */
    .main {
        background-color: #fcfcfc;
    }
    
    /* Títulos con espaciado elegante */
    h1, h2, h3 {
        font-family: 'Inter', 'Segoe UI', sans-serif;
        color: #1a3a5a; /* Azul oscuro del logo */
        font-weight: 300 !important;
        letter-spacing: -0.5px;
    }

    /* Estilo para la información corporativa a la derecha */
    .corporate-info {
        text-align: right;
        border-right: 2px solid #e0e0e0;
        padding-right: 25px;
        margin-top: 50px;
    }

    .corporate-info h3 {
        color: #1a3a5a;
        font-size: 1.1rem;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 10px;
    }

    .corporate-info p {
        color: #666;
        font-size: 0.95rem;
        line-height: 1.6;
        max-width: 500px;
        margin-left: auto; /* Empuja el texto a la derecha */
    }

    /* Botón de WhatsApp Minimalista */
    div.stLinkButton > a {
        background-color: transparent !important;
        color: #25D366 !important;
        border: 1px solid #25D366 !important;
        padding: 0.5rem 1rem !important;
        border-radius: 4px !important;
        transition: 0.3s;
        text-decoration: none !important;
        font-size: 0.8rem !important;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
    div.stLinkButton > a:hover {
        background-color: #25D366 !important;
        color: white !important;
    }

    /* Línea divisoria sutil */
    hr {
        margin: 2em 0;
        border: 0;
        border-top: 1px solid #eee;
    }
    </style>
    """, unsafe_allow_html=True)

# Gestión de logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, 'SALVICLOGO.png')

# --- 3. DATOS (Extraídos del catálogo oficial) ---
@st.cache_data
def cargar_datos_reales():
    # Datos basados fielmente en el catálogo PDF [cite: 192, 206, 263, 296, 308]
    productos = [
        {"Producto": "Sal Refinada Salvic", "Categoría": "Sal", "Presentación": "1kg x 25 / 20kg x 1", "Marca": "Salvic"},
        {"Producto": "Avena en Hojuelas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Lentejas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Caraotas Negras", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Azúcar Refinada", "Categoría": "Dulce", "Presentación": "1kg x 20", "Marca": "Kristal"},
        {"Producto": "Café Gourmet / Premium", "Categoría": "Café", "Presentación": "100gr a 1kg", "Marca": "San Domingo"},
        {"Producto": "Harina de Maíz", "Categoría": "Harinas", "Presentación": "900gr x 10", "Marca": "Masia"},
        {"Producto": "Pastas de Exportación", "Categoría": "Pastas", "Presentación": "500gr a 1kg", "Marca": "América"},
        {"Producto": "Vinagre Blanco", "Categoría": "Salsas", "Presentación": "500ml / 1L / 3.7L", "Marca": "La Delicia"}
    ]
    return pd.DataFrame(productos)

df_salvic = cargar_datos_reales()

# --- 4. SIDEBAR ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True) # Logo único en la esquina superior 
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    menu = st.radio("NAVEGACIÓN", ["HOME", "CATÁLOGO", "CONTACTO"])
    
    st.markdown("---")
    st.caption("RIF: J-29470578-2") [cite: 185]
    st.caption("📍 Envíos Nacionales") [cite: 189]

# --- 5. CONTENIDO ---
if menu == "HOME":
    # Header minimalista
    st.markdown("<h1 style='text-align: center; margin-top: 50px;'>Aliados en tu crecimiento</h1>", unsafe_allow_html=True) [cite: 186]
    
    # Columnas para alinear información a la derecha
    col_izq, col_der = st.columns([1, 1])
    
    with col_der:
        st.markdown(f"""
            <div class="corporate-info">
                <h3>Reseña</h3>
                <p>
                    <b>Distribuidora SALVIC C.A.</b> es una organización dedicada al abastecimiento 
                    estratégico de productos de consumo masivo de alta calidad en Venezuela. 
                    Nuestra infraestructura logística nos permite garantizar una distribución 
                    eficiente a nivel nacional. [cite: 189]
                </p>
                <br>
                <h3>Propuesta de Valor</h3>
                <p>
                    Nos enfocamos en la excelencia operativa y la selección de marcas líderes. 
                    Buscamos simplificar la cadena de suministro de nuestros clientes, ofreciendo 
                    confiabilidad, variedad y una atención personalizada que impulsa su rentabilidad.
                </p>
            </div>
        """, unsafe_allow_html=True)

elif menu == "CATÁLOGO":
    st.markdown("<h1>Catálogo de Productos</h1>", unsafe_allow_html=True)
    
    # Filtros simples
    cat_list = ["Todas"] + sorted(list(df_salvic["Categoría"].unique()))
    cat_select = st.selectbox("Filtrar categoría:", cat_list)
    
    filtered_df = df_salvic if cat_select == "Todas" else df_salvic[df_salvic["Categoría"] == cat_select]
    
    # Tabla minimalista
    st.dataframe(filtered_df, use_container_width=True, hide_index=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("Solicitar cotización", "https://wa.me/584122440691") [cite: 191]

elif menu == "CONTACTO":
    st.markdown("<h1>Contacto Oficial</h1>", unsafe_allow_html=True)
    st.write("📞 0412-2440691") [cite: 191]
    st.write("✉️ salvicdistribuidora@gmail.com") [cite: 205]
    st.write("📸 @salvicdistribuidora") [cite: 190]

# Footer sutil
st.markdown("---")
st.markdown("<p style='text-align: center; color: #aaa; font-size: 0.8rem;'>© 2026 SALVIC C.A. | RIF J-29470578-2</p>", unsafe_allow_html=True) [cite: 185]
