import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SALVIC C.A. | Aliados en tu Crecimiento",
    page_icon="📦",
    layout="wide"
)

# --- 2. CSS PARA TEXTO BLANCO Y DISEÑO MODERNO ---
st.markdown("""
    <style>
    /* Forzar texto blanco en toda la app */
    html, body, [class*="css"], .stMarkdown, h1, h2, h3, p, span, label, li {
        color: white !important;
    }

    /* Estilo para los números de métricas */
    .metric-value {
        font-size: 2.5rem;
        font-weight: bold;
        color: #25D366; /* Un toque de verde éxito */
        text-align: center;
        margin-bottom: 0;
    }
    .metric-label {
        font-size: 1rem;
        text-align: center;
        color: #BDC3C7 !important;
    }

    /* Estilo del botón de descarga PDF */
    div.stDownloadButton > button {
        background-color: #00468b !important;
        color: white !important;
        border: 1px solid white !important;
        border-radius: 8px !important;
        width: 100%;
    }

    /* Tabla legible */
    .stDataFrame { color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# Gestión de archivos
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, 'SALVICLOGO.png')
ruta_pdf = os.path.join(ruta_base, 'CATALOGO SALVIC 2026.pdf')

# --- 3. DATOS ---
@st.cache_data
def cargar_datos():
    productos = [
        {"Producto": "Sal Refinada Salvic", "Categoría": "Sal", "Presentación": "1kg x 25 / 20kg x 1", "Marca": "Salvic"},
        {"Producto": "Avena en Hojuelas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Maíz Cotufa", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Lentejas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Caraotas Negras", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Azúcar Refinada Kristal", "Categoría": "Azúcar", "Presentación": "1kg x 20", "Marca": "Kristal"},
        {"Producto": "Café San Domingo", "Categoría": "Café", "Presentación": "100gr a 1kg", "Marca": "San Domingo"},
        {"Producto": "Arroz Premium", "Categoría": "Arroz", "Presentación": "1kg x 24", "Marca": "Masia"},
        {"Producto": "Harina de Maíz Blanco", "Categoría": "Harina", "Presentación": "900gr x 10", "Marca": "Masia"}
    ]
    return pd.DataFrame(productos)

df_salvic = cargar_datos()

# --- 4. BARRA LATERAL ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    st.markdown("---")
    menu = st.radio("Navegación Principal", ["🏠 Inicio", "🔎 Catálogo", "📞 Contacto"])
    st.markdown("---")
    
    # Botón de Descarga de Catálogo en la Sidebar para que siempre esté a mano
    if os.path.exists(ruta_pdf):
        with open(ruta_pdf, "rb") as f:
            st.download_button(
                label="📥 Descargar Catálogo PDF",
                data=f,
                file_name="CATALOGO_SALVIC_2026.pdf",
                mime="application/pdf"
            )
    st.caption("**RIF:** J-29470578-2")

# --- 5. SECCIÓN: INICIO ---
if menu == "🏠 Inicio":
    st.title("Distribuidora SALVIC C.A.")
    st.subheader("Comprometidos con el abastecimiento nacional.")
    st.write("---")

    # Columnas de Información
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### 📜 Nuestra Reseña")
        st.write("Somos una organización dedicada al abastecimiento estratégico de productos de consumo masivo, garantizando calidad y puntualidad en cada rincón del país.")
    with c2:
        st.markdown("### 💎 Propuesta de Valor")
        st.write("Ofrecemos gestión logística eficiente y personalizada. Somos el aliado estratégico que tu negocio necesita para mantenerse surtido y rentable.")

    st.write("<br>", unsafe_allow_html=True)
    
    # IDEA 1: MÉTRICAS DE CONFIANZA
    st.markdown("---")
    m1, m2, m3 = st.columns(3)
    with m1:
        st.markdown('<p class="metric-value">100%</p><p class="metric-label">Cobertura Nacional</p>', unsafe_allow_html=True)
    with m2:
        st.markdown('<p class="metric-value">+15</p><p class="metric-label">Marcas Líderes</p>', unsafe_allow_html=True)
    with m3:
        st.markdown('<p class="metric-value">24h</p><p class="metric-label">Respuesta Inmediata</p>', unsafe_allow_html=True)
    
    st.write("<br>", unsafe_allow_html=True)

    # IDEA 2: PREGUNTAS FRECUENTES (FAQ)
    with st.expander("❓ Preguntas Frecuentes"):
        st.markdown("""
        * **¿Hacen envíos a todo el país?** Sí, contamos con red logística propia para despachos nacionales.
        * **¿Cuál es el pedido mínimo?** Para consultar cantidades mínimas por producto, contáctanos vía WhatsApp.
        * **¿Qué marcas distribuyen?** Trabajamos con Masia, Gravenca, Kristal, San Domingo, Kellogg's y nuestra marca propia Salvic.
        """)

# --- 6. SECCIÓN: CATÁLOGO ---
elif menu == "🔎 Catálogo":
    st.title("Catálogo de Productos 2026")
    
    busqueda = st.text_input("Buscar producto o marca...", placeholder="Ej: Harina, Masia...")
    
    res = df_salvic.copy()
    if busqueda:
        res = res[res["Producto"].str.contains(busqueda, case=False) | res["Marca"].str.contains(busqueda, case=False)]
    
    st.dataframe(res, use_container_width=True, hide_index=True)
    
    st.markdown("### 📲 Inicia tu pedido")
    st.link_button("💬 Consultar por WhatsApp", "https://wa.me/584122440691")

# --- 7. SECCIÓN: CONTACTO ---
elif menu == "📞 Contacto":
    st.title("Canales de Atención")
    st.write("---")
    st.markdown("""
    * **📞 Teléfono:** 0412-2440691
    * **✉️ Email:** salvicdistribuidora@gmail.com
    * **📸 Instagram:** [@salvicdistribuidora](https://instagram.com/salvicdistribuidora)
    """)

st.markdown("---")
st.caption("© 2026 Distribuidora SALVIC C.A. | RIF J-29470578-2")
