import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Distribuidora SALVIC C.A | Catálogo 2026",
    page_icon="📦",
    layout="wide"
)

# Estilo personalizado para el botón de WhatsApp verde
st.markdown("""
    <style>
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border: none !important;
        padding: 10px 20px !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        text-decoration: none !important;
        display: inline-flex !important;
        align-items: center !important;
    }
    div.stLinkButton > a:hover {
        background-color: #128C7E !important;
        color: white !important;
    }
    </style>
    """, unsafe_allow_html=True)

ruta_base = os.path.dirname(__file__)
# Asegúrate de que el archivo se llame exactamente SALVICLOGO.jpg en tu carpeta
ruta_logo = os.path.join(ruta_base, 'SALVICLOGO.jpg')

# --- 2. CARGA DE DATOS REALES ---
@st.cache_data
def cargar_catalogo_salvic():
    productos = [
        {"Producto": "Sal Refinada Salvic", "Categoría": "Sal", "Presentación": "1kg x 25 / 20kg x 1", "Marca": "Salvic"},
        {"Producto": "Avena en Hojuelas", "Categoría": "Granos/Cereales", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Maíz Cotufa", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Lentejas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Caraotas Negras", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Azúcar Refinada Kristal", "Categoría": "Azúcar", "Presentación": "1kg x 20", "Marca": "Kristal"},
        {"Producto": "Café San Domingo (Gourmet/Premium)", "Categoría": "Café", "Presentación": "100gr a 500gr / 1kg", "Marca": "San Domingo"},
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

df_salvic = cargar_catalogo_salvic()

# --- 3. BARRA LATERAL ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    else:
        st.markdown(f"### **SALVIC C.A.**")
    
    st.markdown(f"**RIF: J-29470578-2**") [cite: 1, 8, 27]
    st.markdown("---")
    menu = st.radio("Secciones:", ["Inicio", "Catálogo Interactivo", "Contacto"])
    st.markdown("---")
    st.info("📦 Envíos a todo el país") [cite: 5]

# --- 4. SECCIÓN: INICIO ---
if menu == "Inicio":
    st.title("Distribuidora SALVIC C.A.")
    st.subheader("¡Aliados en tu crecimiento!")
    
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, width=400)
    
    col_hist, col_val = st.columns(2)
    with col_hist:
        st.markdown("### 📜 Reseña Histórica")
        st.write("Distribuidora SALVIC C.A. nace con el compromiso de ofrecer productos alimenticios de primera calidad en todo el territorio nacional.")
        
    with col_val:
        st.markdown("### 💎 Propuesta de Valor")
        st.write("Nos enfocamos en la eficiencia logística y en brindar marcas de confianza para el hogar venezolano.")

# --- 5. SECCIÓN: CATÁLOGO ---
elif menu == "Catálogo Interactivo":
    st.title("🔎 Nuestro Catálogo")
    
    c1, c2 = st.columns([3, 1])
    with c1:
        query = st.text_input("¿Qué producto buscas?", placeholder="Ej: Café, Harina, Caraotas...")
    with c2:
        cat = st.selectbox("Categoría:", ["Todas"] + list(df_salvic["Categoría"].unique()))
    
    df_res = df_salvic.copy()
    if query:
        df_res = df_res[df_res["Producto"].str.contains(query, case=False) | df_res["Marca"].str.contains(query, case=False)]
    if cat != "Todas":
        df_res = df_res[df_res["Categoría"] == cat]
        
    st.dataframe(df_res, use_container_width=True, hide_index=True)
    
    st.markdown("### 📲 ¿Listo para hacer un pedido?")
    wa_link = "https://wa.me/584122440691?text=Hola,%20quisiera%20consultar%20precios%20del%20catálogo" [cite: 7]
    st.link_button("💬 Contactar por WhatsApp", wa_link)

# --- 6. SECCIÓN: CONTACTO ---
elif menu == "Contacto":
    st.title("📩 Canales de Atención")
    st.write("📍 **Ubicación:** Venezuela (Envíos a nivel nacional)") [cite: 5]
    st.write("📞 **Teléfono:** 0412-2440691") [cite: 7]
    st.write("✉️ **Email:** salvicdistribuidora@gmail.com") [cite: 21, 51]
    st.write("📸 **Instagram:** @salvicdistribuidora") [cite: 6]

st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} Distribuidora SALVIC C.A. | RIF J-29470578-2") [cite: 1, 8, 27]
