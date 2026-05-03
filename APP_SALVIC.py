import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SALVIC C.A. | Catálogo 2026",
    page_icon="📦",
    layout="wide"
)

# --- 2. CSS PARA FONDO BLANCO Y TEXTO LEGIBLE ---
st.markdown("""
    <style>
    /* Forzar fondo blanco en toda la app */
    .stApp {
        background-color: white !important;
    }

    /* Forzar color de texto gris oscuro/profesional para que se vea siempre */
    .texto-derecha {
        text-align: right;
        color: #2c3e50 !important;
        line-height: 1.8;
        font-family: 'Inter', sans-serif;
    }

    .titulo-derecha {
        text-align: right;
        color: #1a3a5a !important;
        font-weight: 600;
        margin-bottom: 5px;
        text-transform: uppercase;
        letter-spacing: 1px;
    }

    /* Línea divisoria sutil a la derecha */
    .contenedor-info {
        border-right: 2px solid #f0f0f0;
        padding-right: 20px;
        margin-top: 30px;
    }

    /* Botón WhatsApp */
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border: none !important;
        font-weight: bold !important;
        padding: 0.5rem 1rem !important;
        border-radius: 8px !important;
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
        {"Producto": "Caraotas Negras", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Azúcar Refinada", "Categoría": "Azúcar", "Presentación": "1kg x 20", "Marca": "Kristal"},
        {"Producto": "Café San Domingo", "Categoría": "Café", "Presentación": "500gr", "Marca": "San Domingo"},
        {"Producto": "Arroz Premium", "Categoría": "Arroz", "Presentación": "1kg x 24", "Marca": "Masia"},
        {"Producto": "Harina de Maíz Blanco", "Categoría": "Harina", "Presentación": "900gr x 10", "Marca": "Masia"}
    ]
    return pd.DataFrame(productos)

df_salvic = cargar_datos()

# --- 4. BARRA LATERAL (Limpia y profesional) ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    menu = st.radio("Navegación", ["🏠 Inicio", "🔎 Catálogo", "📞 Contacto"])
    st.markdown("---")
    st.caption("RIF: J-29470578-2")

# --- 5. SECCIÓN: INICIO (Alineado a la derecha sobre fondo blanco) ---
if menu == "🏠 Inicio":
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # Columnas: Izquierda vacía para empujar el contenido a la derecha
    col_vacia, col_contenido = st.columns([1, 2])
    
    with col_contenido:
        st.markdown("""
            <div class="contenedor-info">
                <h3 class="titulo-derecha">Nuestra Reseña</h3>
                <p class="texto-derecha">
                    <b>Distribuidora SALVIC C.A.</b> es una empresa venezolana dedicada al 
                    abastecimiento estratégico de productos de primera necesidad. 
                    Nuestra misión es conectar calidad con eficiencia logística, garantizando 
                    que cada producto llegue a su destino en tiempo récord en todo el territorio nacional.
                </p>
                <br>
                <h3 class="titulo-derecha">Propuesta de Valor</h3>
                <p class="texto-derecha">
                    Nos enfocamos en ser tu <b>aliado de confianza</b>. No solo distribuimos marcas, 
                    construimos relaciones basadas en la puntualidad, la transparencia y una 
                    selección rigurosa de productos que garantizan la satisfacción de tus clientes finales.
                </p>
            </div>
        """, unsafe_allow_html=True)

# --- 6. SECCIÓN: CATÁLOGO ---
elif menu == "🔎 Catálogo":
    st.title("Catálogo de Productos")
    busqueda = st.text_input("¿Qué buscas hoy?", placeholder="Ej: Café, Harina...")
    
    res = df_salvic.copy()
    if busqueda:
        res = res[res["Producto"].str.contains(busqueda, case=False) | res["Marca"].str.contains(busqueda, case=False)]
    
    st.dataframe(res, use_container_width=True, hide_index=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("💬 Consultar por WhatsApp", "https://wa.me/584122440691")

# --- 7. SECCIÓN: CONTACTO ---
elif menu == "📞 Contacto":
    st.title("Atención al Cliente")
    st.write("📞 **Teléfono:** 0412-2440691")
    st.write("✉️ **Email:** salvicdistribuidora@gmail.com")
    st.write("📸 **Instagram:** [@salvicdistribuidora](https://instagram.com/salvicdistribuidora)")

# Footer sutil
st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} Distribuidora SALVIC C.A. | RIF J-29470578-2")
