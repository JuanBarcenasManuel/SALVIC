import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SALVIC C.A. | Catálogo 2026",
    page_icon="📦",
    layout="wide"
)

# --- 2. ESTILOS (Volviendo a lo que funcionaba: Blanco y profesional) ---
st.markdown("""
    <style>
    /* Forzar fondo blanco en toda la aplicación */
    .stApp {
        background-color: white !important;
    }

    /* Estilo de las tarjetas de información (Gris muy claro para que resalten sobre el blanco) */
    .info-card {
        background-color: #fcfcfc;
        padding: 2rem;
        border-radius: 15px;
        border-right: 5px solid #00468b; /* Borde a la derecha como pediste */
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
        text-align: right; /* Alineación del texto a la derecha */
    }

    /* Forzar que los títulos y párrafos sean azul oscuro / gris para legibilidad */
    .info-card h3 {
        color: #00468b !important;
        margin-bottom: 10px;
    }

    .info-card p {
        color: #333333 !important;
        line-height: 1.6;
    }

    /* Botón de WhatsApp institucional */
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        text-decoration: none !important;
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
    st.markdown("---")
    menu = st.radio("Navegación", ["🏠 Inicio", "🔎 Catálogo", "📞 Contacto"])
    st.markdown("---")
    st.caption("RIF: J-29470578-2")

# --- 5. SECCIÓN: INICIO (Con los bloques a la derecha como antes) ---
if menu == "🏠 Inicio":
    st.title("Distribuidora SALVIC C.A.")
    st.subheader("¡Aliados en tu crecimiento!")
    
    # Creamos dos columnas: la izquierda vacía para empujar el contenido a la derecha
    col_vacia, col_contenido = st.columns([1, 2])
    
    with col_contenido:
        # Bloque de Reseña
        st.markdown("""
        <div class="info-card">
            <h3>📜 Nuestra Reseña</h3>
            <p>
                <b>Distribuidora SALVIC C.A.</b> es una empresa venezolana dedicada al 
                abastecimiento estratégico de productos de primera necesidad. 
                Nuestra misión es conectar calidad con eficiencia logística, garantizando 
                que cada producto llegue a su destino en tiempo récord en todo el territorio nacional.
            </p>
        </div>
        """, unsafe_allow_html=True)

        # Bloque de Propuesta de Valor
        st.markdown("""
        <div class="info-card">
            <h3>💎 Propuesta de Valor</h3>
            <p>
                Nos enfocamos en ser tu <b>aliado de confianza</b>. No solo distribuimos marcas, 
                construimos relaciones basadas en la puntualidad, la transparencia y una 
                selección rigurosa de productos que garantizan la satisfacción de tus clientes finales.
            </p>
        </div>
        """, unsafe_allow_html=True)

# --- 6. SECCIÓN: CATÁLOGO ---
elif menu == "🔎 Catálogo":
    st.title("Catálogo de Productos")
    busqueda = st.text_input("Buscar producto o marca...")
    
    res = df_salvic.copy()
    if busqueda:
        res = res[res["Producto"].str.contains(busqueda, case=False) | res["Marca"].str.contains(busqueda, case=False)]
    
    st.dataframe(res, use_container_width=True, hide_index=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("💬 Consultar por WhatsApp", "https://wa.me/584122440691")

# --- 7. SECCIÓN: CONTACTO ---
elif menu == "📞 Contacto":
    st.title("Canales de Atención")
    st.write("📞 **Teléfono:** 0412-2440691")
    st.write("✉️ **Email:** salvicdistribuidora@gmail.com")
    st.write("📸 **Instagram:** @salvicdistribuidora")

st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} Distribuidora SALVIC C.A.")
