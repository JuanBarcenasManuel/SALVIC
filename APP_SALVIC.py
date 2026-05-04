import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SALVIC C.A. | Catálogo 2026",
    page_icon="📦",
    layout="wide"
)

# --- 2. CSS PARA TEXTO BLANCO TOTAL (Solución Legibilidad) ---
st.markdown("""
    <style>
    /* Forzamos TODO el texto a blanco: títulos, párrafos, widgets y sidebar */
    html, body, [class*="css"], .stMarkdown, h1, h2, h3, p, span, label, li {
        color: white !important;
    }

    /* Ajuste para que las tablas (Dataframes) también muestren texto blanco */
    .stDataFrame, [data-testid="stTable"] {
        color: white !important;
    }

    /* El botón de WhatsApp lo dejamos verde para que resalte y sea funcional */
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border: none !important;
        padding: 0.6rem 1.2rem !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        text-decoration: none !important;
    }
    
    /* Input de búsqueda con texto legible */
    input {
        color: black !important; /* El interior del buscador sí en negro para escribir bien */
    }
    </style>
    """, unsafe_allow_html=True)

# Gestión de logo
ruta_base = os.path.dirname(__file__)
ruta_logo = os.path.join(ruta_base, 'SALVICLOGO.png')

# --- 3. DATOS DEL CATÁLOGO (Completos) ---
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

# --- 4. BARRA LATERAL ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    else:
        st.title("SALVIC C.A.")
    
    st.markdown("---")
    menu = st.radio("Navegación", ["🏠 Inicio", "🔎 Catálogo Interactivo", "📞 Contacto"])
    st.markdown("---")
    st.caption("**RIF:** J-29470578-2")

# --- 5. SECCIÓN: INICIO ---
if menu == "🏠 Inicio":
    st.title("Distribuidora SALVIC C.A.")
    st.subheader("¡Aliados en tu crecimiento!")
    
    st.write("---")
    
    # Texto en blanco directo, sin rectángulos molestos
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### 📜 Nuestra Reseña")
        st.write("""
            **Distribuidora SALVIC C.A.** es una empresa venezolana consolidada con el RIF J-29470578-2, 
            nacida con la misión de abastecer hogares y comercios con productos de la canasta básica de la 
            más alta calidad. Con una sólida red logística, garantizamos el alcance nacional.
        """)

    with col2:
        st.markdown("### 💎 Propuesta de Valor")
        st.write("""
            Nos diferenciamos por ofrecer una **gestión logística eficiente y personalizada**. 
            Nuestra propuesta se basa en: variedad competitiva, atención directa y el compromiso 
            de ser el aliado estratégico que tu negocio necesita para crecer.
        """)

# --- 6. SECCIÓN: CATÁLOGO ---
elif menu == "🔎 Catálogo Interactivo":
    st.title("Catálogo de Productos 2026")
    
    c1, c2 = st.columns([3, 1])
    with c1:
        busqueda = st.text_input("¿Qué necesitas hoy?", placeholder="Ej: Harina, Café...")
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
    st.link_button("💬 Consultar precios por WhatsApp", "https://wa.me/584122440691?text=Hola, quisiera un presupuesto")

# --- 7. SECCIÓN: CONTACTO ---
elif menu == "📞 Contacto":
    st.title("Canales Oficiales")
    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown(f"""
        - **📍 Ubicación:** Envíos a Nivel Nacional
        - **📞 Teléfono:** 0412-2440691 
        - **✉️ Email:** salvicdistribuidora@gmail.com
        """)
    with col_b:
        st.markdown("- **📸 Instagram:** [@salvicdistribuidora](https://instagram.com/salvicdistribuidora)")

st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} Distribuidora SALVIC C.A. | RIF J-29470578-2")
