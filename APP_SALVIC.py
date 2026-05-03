import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="Distribuidora SALVIC C.A | Catálogo 2026",
    page_icon="📦",
    layout="wide"
)

# Estilo para el botón de WhatsApp verde
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
    }
    div.stLinkButton > a:hover {
        background-color: #128C7E !important;
    }
    </style>
    """, unsafe_allow_html=True)

ruta_base = os.path.dirname(__file__)
# Ajustado a .png según tu captura de GitHub
ruta_logo = os.path.join(ruta_base, 'SALVICLOGO.png')

# --- 2. CARGA DE DATOS ---
@st.cache_data
def cargar_catalogo_salvic():
    productos = [
        {"Producto": "Sal Refinada Salvic", "Categoría": "Sal", "Presentación": "1kg x 25 / 20kg x 1", "Marca": "Salvic"},
        {"Producto": "Avena en Hojuelas", "Categoría": "Granos/Cereales", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Maíz Cotufa", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca"},
        {"Producto": "Lentejas", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Caraotas Negras", "Categoría": "Granos", "Presentación": "400gr x 20", "Marca": "Gravenca / Salvic"},
        {"Producto": "Azúcar Refinada Kristal", "Categoría": "Azúcar", "Presentación": "1kg x 20", "Marca": "Kristal"},
        {"Producto": "Café San Domingo", "Categoría": "Café", "Presentación": "100gr a 1kg", "Marca": "San Domingo"},
        {"Producto": "Café La Protectora", "Categoría": "Café", "Presentación": "250gr / 500gr", "Marca": "La Protectora"},
        {"Producto": "Arroz Premium", "Categoría": "Arroz", "Presentación": "1kg x 24", "Marca": "Masia"},
        {"Producto": "Harina de Maíz Blanco", "Categoría": "Harina", "Presentación": "900gr x 10", "Marca": "Masia"},
        {"Producto": "Pastas América", "Categoría": "Pastas", "Presentación": "500gr a 1kg", "Marca": "América"},
        {"Producto": "Margarina La Delicia", "Categoría": "Grasas", "Presentación": "250gr / 500gr", "Marca": "La Delicia"},
        {"Producto": "Vinagre Blanco", "Categoría": "Salsas", "Presentación": "500ml / 1Lt", "Marca": "La Delicia"},
        {"Producto": "Salsas (Ajo, Soya, Inglesa)", "Categoría": "Salsas", "Presentación": "150ml x 24", "Marca": "La Delicia"},
        {"Producto": "Cereales Kellogg's", "Categoría": "Cereales", "Presentación": "Variadas", "Marca": "Kellogg's"}
    ]
    return pd.DataFrame(productos)

df_salvic = cargar_catalogo_salvic()

# --- 3. BARRA LATERAL ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    
    st.markdown("### **RIF: J-29470578-2**")
    st.markdown("---")
    menu = st.radio("Secciones:", ["Inicio", "Catálogo Interactivo", "Contacto"])

# --- 4. SECCIÓN: INICIO ---
if menu == "Inicio":
    st.title("Distribuidora SALVIC C.A.")
    st.subheader("¡Aliados en tu crecimiento!")
    
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, width=300)
    
    st.markdown("### 📜 Reseña Histórica")
    st.write("Distribuidora SALVIC C.A. es una empresa dedicada a la comercialización de productos de consumo masivo con envíos a todo el país.")

# --- 5. SECCIÓN: CATÁLOGO ---
elif menu == "Catálogo Interactivo":
    st.title("🔎 Nuestro Catálogo")
    query = st.text_input("Buscar producto o marca:")
    
    df_res = df_salvic.copy()
    if query:
        df_res = df_res[df_res["Producto"].str.contains(query, case=False) | df_res["Marca"].str.contains(query, case=False)]
        
    st.dataframe(df_res, use_container_width=True, hide_index=True)
    
    st.markdown("### 📲 ¿Hacer un pedido?")
    wa_link = "https://wa.me/584122440691?text=Hola,%20solicito%20información"
    st.link_button("💬 WhatsApp Ventas", wa_link)

# --- 6. SECCIÓN: CONTACTO ---
elif menu == "Contacto":
    st.title("📩 Contacto")
    st.write("📞 **Teléfono:** 0412-2440691")
    st.write("✉️ **Email:** salvicdistribuidora@gmail.com")

st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} Distribuidora SALVIC C.A. | RIF J-29470578-2")
