import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SALVIC C.A. | Catálogo 2026",
    page_icon="📦",
    layout="wide"
)

# --- 2. CSS ANTI-MODO OSCURO (CORRECCIÓN TOTAL) ---
st.markdown("""
    <style>
    /* 1. Forzar fondo blanco en toda la app y sidebar */
    .stApp, [data-testid="stSidebar"], .stHeader {
        background-color: white !important;
    }

    /* 2. Forzar que TODO el texto sea gris oscuro/negro para que se lea */
    h1, h2, h3, p, span, label, .stMarkdown {
        color: #1a1a1a !important;
    }

    /* 3. Estilo de las tarjetas (ahora con fondo gris muy claro para contraste) */
    .info-card {
        background-color: #f8f9fa !important;
        padding: 2rem;
        border-radius: 15px;
        border-right: 5px solid #00468b;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
        text-align: right;
    }
    
    .info-card h3 { color: #00468b !important; }
    .info-card p { color: #333333 !important; }

    /* 4. Corrección de la Tabla (Catálogo) */
    .stDataFrame, [data-testid="stTable"] {
        background-color: white !important;
        color: black !important;
    }

    /* 5. Botón WhatsApp */
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Gestión de logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, 'SALVICLOGO.png')

# --- 3. DATOS ---
@st.cache_data
def cargar_datos():
    productos = [
        {"Producto": "Sal Refinada Salvic", "Categoría": "Sal", "Presentación": "1kg x 25 / 20kg x 1", "Marca": "Salvic"},
        {"Producto": "Avena en Hojuelas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Lentejas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Caraotas Negras", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Salvic"},
        {"Producto": "Azúcar Refinada", "Categoría": "Azúcar", "Presentación": "1kg x 20", "Marca": "Kristal"},
        {"Producto": "Café San Domingo", "Categoría": "Café", "Presentación": "500gr", "Marca": "San Domingo"},
        {"Producto": "Arroz Premium", "Categoría": "Arroz", "Presentación": "1kg x 24", "Marca": "Masia"},
        {"Producto": "Harina de Maíz Blanco", "Categoría": "Harina", "Presentación": "900gr x 10", "Marca": "Masia"}
    ]
    return pd.DataFrame(productos)

df_salvic = cargar_datos()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    menu = st.radio("MENÚ PRINCIPAL", ["🏠 Inicio", "🔎 Catálogo", "📞 Contacto"])
    st.markdown("---")
    st.markdown("<span style='color:black;'><b>RIF:</b> J-29470578-2</span>", unsafe_allow_html=True)

# --- 5. SECCIÓN: INICIO ---
if menu == "🏠 Inicio":
    st.title("Distribuidora SALVIC C.A.")
    
    col_vacia, col_contenido = st.columns([1, 2])
    
    with col_contenido:
        st.markdown("""
        <div class="info-card">
            <h3>📜 Nuestra Reseña</h3>
            <p>
                <b>Distribuidora SALVIC C.A.</b> es una empresa dedicada al 
                abastecimiento estratégico de productos de primera necesidad. 
                Garantizamos que cada producto llegue a su destino en tiempo récord nacional.
            </p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("""
        <div class="info-card">
            <h3>💎 Propuesta de Valor</h3>
            <p>
                Nos enfocamos en ser tu <b>aliado de confianza</b>. Construimos relaciones 
                basadas en la puntualidad, la transparencia y una selección rigurosa de productos.
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- 6. SECCIÓN: CATÁLOGO ---
elif menu == "🔎 Catálogo":
    st.markdown("<h2 style='color:black;'>Catálogo de Productos</h2>", unsafe_allow_html=True)
    busqueda = st.text_input("Buscar producto...")
    
    res = df_salvic.copy()
    if busqueda:
        res = res[res["Producto"].str.contains(busqueda, case=False)]
    
    # Tabla forzada a colores claros
    st.dataframe(res, use_container_width=True, hide_index=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("💬 Consultar por WhatsApp", "https://wa.me/584122440691")

# --- 7. SECCIÓN: CONTACTO ---
elif menu == "📞 Contacto":
    st.markdown("<h2 style='color:black;'>Canales de Atención</h2>", unsafe_allow_html=True)
    st.markdown("""
        <div style="background-color: #f8f9fa; padding: 20px; border-radius: 10px;">
            <p style="color: black !important;">📞 <b>Teléfono:</b> 0412-2440691</p>
            <p style="color: black !important;">✉️ <b>Email:</b> salvicdistribuidora@gmail.com</p>
            <p style="color: black !important;">📸 <b>Instagram:</b> @salvicdistribuidora</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("© 2026 Distribuidora SALVIC C.A. | Todos los derechos reservados.")
