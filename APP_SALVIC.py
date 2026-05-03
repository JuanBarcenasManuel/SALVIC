import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SALVIC C.A. | Catálogo 2026",
    page_icon="📦",
    layout="wide"
)

# --- 2. ESTILOS PERSONALIZADOS (CSS) ---
st.markdown("""
    <style>
    /* Color de fondo y tipografía general */
    .main {
        background-color: #f8f9fa;
    }
    
    /* Estilo para el botón de WhatsApp institucional */
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        transition: 0.3s;
        text-decoration: none !important;
        display: inline-flex !important;
        align-items: center !important;
    }
    div.stLinkButton > a:hover {
        background-color: #128C7E !important;
        transform: scale(1.05);
    }

    /* Estilo para las tarjetas de información */
    .info-card {
        background-color: white;
        padding: 2rem;
        border-radius: 15px;
        border-left: 5px solid #00468b;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        margin-bottom: 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# Gestión de logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, 'SALVICLOGO.png')

# --- 3. DATOS DEL CATÁLOGO ---
@st.cache_data
def cargar_datos():
    productos = [
        {"Producto": "Sal Refinada Salvic", "Categoría": "Sal", "Presentación": "1kg x 25 / 20kg x 1", "Marca": "Salvic"},
        {"Producto": "Avena en Hojuelas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Maíz Cotufa", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Lentejas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Caraotas Negras", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Azúcar Refinada Kristal", "Categoría": "Azúcar", "Presentación": "1kg x 20", "Marca": "Kristal"},
        {"Producto": "Café San Domingo (Gourmet/Premium)", "Categoría": "Café", "Presentación": "100gr a 1kg", "Marca": "San Domingo"},
        {"Producto": "Café La Protectora", "Categoría": "Café", "Presentación": "250gr / 500gr", "Marca": "La Protectora"},
        {"Producto": "Arroz Premium", "Categoría": "Arroz", "Presentación": "1kg x 24", "Marca": "Masia"},
        {"Producto": "Harina de Maíz Blanco", "Categoría": "Harina", "Presentación": "900gr x 10", "Marca": "Masia"},
        {"Producto": "Pastas América (Varias)", "Categoría": "Pastas", "Presentación": "500gr a 1kg", "Marca": "América"},
        {"Producto": "Margarina La Delicia", "Categoría": "Grasas", "Presentación": "250gr / 500gr", "Marca": "La Delicia"},
        {"Producto": "Vinagre Blanco", "Categoría": "Salsas", "Presentación": "500ml / 1Lt / 3.785Lt", "Marca": "La Delicia"},
        {"Producto": "Salsas (Ajo, Soya, Inglesa)", "Categoría": "Salsas", "Presentación": "150ml x 24", "Marca": "La Delicia"},
        {"Producto": "Cereales Kellogg's", "Categoría": "Cereales", "Presentación": "Variadas", "Marca": "Kellogg's"}
    ]
    return pd.DataFrame(productos)

df_salvic = cargar_datos()

# --- 4. BARRA LATERAL (Navegación Limpia) ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    else:
        st.title("SALVIC C.A.")
    
    st.markdown("---")
    menu = st.radio("Navegación", ["🏠 Inicio", "🔎 Catálogo Interactivo", "📞 Contacto"])
    st.markdown("---")
    st.caption("**RIF:** J-29470578-2")
    st.info("🚚 Envíos a todo el país")

# --- 5. SECCIÓN: INICIO ---
# --- 5. SECCIÓN: INICIO (Minimalista y Limpia) ---
if menu == "🏠 Inicio":
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Título con el azul de tu logo, pero sin cajas
    st.markdown("<h1 style='color: #00468b; margin-bottom: 0;'>Distribuidora SALVIC C.A.</h1>", unsafe_allow_html=True)
    st.markdown("<p style='font-size: 1.1rem; color: #666;'>Aliados en tu crecimiento</p>", unsafe_allow_html=True)
    
    st.markdown("---") # Una línea divisoria sutil
    
    # Usamos columnas solo para organizar el texto, sin fondos de colores
    col1, col2 = st.columns(2)

    with col1:
        st.markdown("""
            <div style="padding-right: 20px;">
                <h3 style="color: #00468b;">📜 Nuestra Reseña</h3>
                <p style="color: #1a1a1a; line-height: 1.6; text-align: justify;">
                    <b>Distribuidora SALVIC C.A.</b> es una organización venezolana 
                    dedicada al abastecimiento de productos de la canasta básica de la más alta calidad. 
                    Nuestra red logística garantiza una distribución eficiente 
                    en todo el territorio nacional, trabajando con marcas líderes para asegurar 
                    la excelencia en cada entrega.
                </p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("""
            <div style="padding-left: 20px; border-left: 1px solid #eee;">
                <h3 style="color: #00468b;">💎 Propuesta de Valor</h3>
                <p style="color: #1a1a1a; line-height: 1.6; text-align: justify;">
                    Nos diferenciamos por una <b>gestión logística personalizada</b>. 
                    Nuestra propuesta se fundamenta en la variedad competitiva, 
                    la atención directa y el compromiso de ser el soporte que 
                    tu inventario necesita para mantenerse siempre surtido y rentable.
                </p>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    st.info("🚚 Envíos a todo el país | RIF: J-29470578-2")
# --- 6. SECCIÓN: CATÁLOGO ---
elif menu == "🔎 Catálogo Interactivo":
    st.title("Catálogo de Productos 2026")
    
    c1, c2 = st.columns([3, 1])
    with c1:
        busqueda = st.text_input("¿Qué necesitas hoy?", placeholder="Ej: Harina Masia, Café...")
    with c2:
        filtro_cat = st.selectbox("Categoría", ["Todas"] + sorted(list(df_salvic["Categoría"].unique())))

    # Filtrado
    res = df_salvic.copy()
    if busqueda:
        res = res[res["Producto"].str.contains(busqueda, case=False) | res["Marca"].str.contains(busqueda, case=False)]
    if filtro_cat != "Todas":
        res = res[res["Categoría"] == filtro_cat]

    st.dataframe(res, use_container_width=True, hide_index=True)
    
    st.markdown("### 📲 Inicia tu pedido")
    st.link_button("💬 Consultar precios por WhatsApp", "https://wa.me/584122440691?text=Hola,%20quisiera%20un%20presupuesto")

# --- 7. SECCIÓN: CONTACTO ---
elif menu == "📞 Contacto":
    st.title("Canales Oficiales")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"""
        - **📍 Ubicación:** Envíos a Nivel Nacional [cite: 189]
        - **📞 Teléfono:** 0412-2440691 
        - **✉️ Email:** salvicdistribuidora@gmail.com [cite: 205]
        """)
    with col2:
        st.markdown("- **📸 Instagram:** [@salvicdistribuidora](https://instagram.com/salvicdistribuidora) [cite: 190]")

st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} Distribuidora SALVIC C.A. | RIF J-29470578-2")
