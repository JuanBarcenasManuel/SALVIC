import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SALVIC C.A. | Catálogo",
    page_icon="📦",
    layout="wide"
)

# --- 2. CSS PARA MINIMALISMO ABSOLUTO ---
st.markdown("""
    <style>
    /* Fondo gris muy sutil para que el contenido blanco resalte */
    .main {
        background-color: #f4f7f9;
    }
    
    /* Tipografía */
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;600&display=swap');
    html, body, [class*="css"] {
        font-family: 'Montserrat', sans-serif;
    }

    /* Contenedor de información alineado a la derecha */
    .right-container {
        text-align: right;
        padding: 40px;
        background-color: transparent;
        border-right: 1px solid #1a3a5a; /* Línea fina azul oscuro */
        margin-right: 20px;
    }

    .title-salvic {
        color: #1a3a5a;
        font-weight: 600;
        letter-spacing: 2px;
        text-transform: uppercase;
        font-size: 1.5rem;
        margin-bottom: 20px;
    }

    .text-body {
        color: #555;
        font-weight: 300;
        line-height: 1.8;
        font-size: 1rem;
        max-width: 600px;
        margin-left: auto;
    }

    /* Botón WhatsApp Minimalista (Outline) */
    div.stLinkButton > a {
        background-color: transparent !important;
        color: #25D366 !important;
        border: 1px solid #25D366 !important;
        border-radius: 2px !important;
        padding: 10px 25px !important;
        font-size: 12px !important;
        letter-spacing: 1px !important;
        text-transform: uppercase !important;
        transition: 0.4s !important;
    }
    div.stLinkButton > a:hover {
        background-color: #25D366 !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, 'SALVICLOGO.png')

# --- 3. BARRA LATERAL (Limpia) ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    st.markdown("<br><br>", unsafe_allow_html=True)
    menu = st.radio("", ["HOME", "PRODUCTOS", "CONTACTO"])
    st.markdown("---")
    st.caption("RIF: J-29470578-2")

# --- 4. SECCIÓN: HOME ---
if menu == "HOME":
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Usamos 3 columnas para empujar todo a la derecha
    col1, col2, col3 = st.columns([1, 0.2, 2])
    
    with col3:
        st.markdown("""
            <div class="right-container">
                <div class="title-salvic">Distribuidora SALVIC C.A.</div>
                <p class="text-body">
                    <b>Excelencia en Suministros.</b><br>
                    Somos un eslabón estratégico en la cadena de comercialización de alimentos 
                    en Venezuela. Nuestra operación se define por la puntualidad y la 
                    selección rigurosa de productos que cumplen con los más altos estándares.
                </p>
                <br><br>
                <div class="title-salvic" style="font-size: 1.2rem;">Propuesta de Valor</div>
                <p class="text-body">
                    Convertimos la logística en una ventaja competitiva para nuestros clientes. 
                    Garantizamos un flujo constante de mercancía con una atención personalizada 
                    que entiende la dinámica del mercado nacional.
                </p>
            </div>
        """, unsafe_allow_html=True)

# --- 5. SECCIÓN: PRODUCTOS ---
elif menu == "PRODUCTOS":
    st.markdown("<h2 style='color: #1a3a5a; font-weight: 300;'>Catálogo de Disponibilidad</h2>", unsafe_allow_html=True)
    
    # Simulando carga de datos rápida
    df = pd.DataFrame([
        {"Producto": "Sal Refinada Salvic", "Presentación": "1kg x 25", "Marca": "Salvic"},
        {"Producto": "Avena en Hojuelas", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Café San Domingo", "Presentación": "500gr", "Marca": "San Domingo"},
        {"Producto": "Arroz Premium", "Presentación": "1kg x 24", "Marca": "Masia"}
    ])
    
    st.dataframe(df, use_container_width=True, hide_index=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("Solicitar Lista de Precios", "https://wa.me/584122440691")

# --- 6. SECCIÓN: CONTACTO ---
elif menu == "CONTACTO":
    st.markdown("<h2 style='color: #1a3a5a; font-weight: 300;'>Contacto</h2>", unsafe_allow_html=True)
    st.write("✉️ salvicdistribuidora@gmail.com")
    st.write("📞 0412-2440691")

st.markdown("---")
st.caption("© 2026 SALVIC C.A. | Distribución Nacional")
