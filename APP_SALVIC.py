import streamlit as st
import pandas as pd
import os

# --- 1. CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(
    page_title="SALVIC C.A. | Catálogo 2026",
    page_icon="📦",
    layout="wide"
)

# --- 2. ESTILOS PROFESIONALES (AZUL CLARO & GRIS) ---
st.markdown("""
    <style>
    /* Tipografía y fondo */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #4A4A4A;
    }

    .main {
        background-color: #FDFDFD;
    }

    /* Banner Hero (Sustituye a los logos repetidos) */
    .hero-section {
        background: linear-gradient(135deg, #E3F2FD 0%, #F5F5F5 100%);
        padding: 4rem 2rem;
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 1px solid #E0E0E0;
    }

    /* Alineación de texto derecha para propuesta de valor */
    .text-right {
        text-align: right;
    }

    /* Tarjetas Minimalistas */
    .pro-card {
        background-color: white;
        padding: 1.5rem;
        border-radius: 12px;
        border-right: 4px solid #90CAF9; /* Azul claro del logo */
        box-shadow: 0 2px 10px rgba(0,0,0,0.05);
        margin-bottom: 1.5rem;
    }

    /* Botón WhatsApp Estilizado */
    div.stLinkButton > a {
        background-color: #25D366 !important;
        color: white !important;
        border: none !important;
        padding: 0.8rem 1.5rem !important;
        border-radius: 50px !important;
        font-weight: 600 !important;
        transition: all 0.3s ease;
        text-decoration: none !important;
    }
    div.stLinkButton > a:hover {
        background-color: #128C7E !important;
        box-shadow: 0 4px 12px rgba(37, 211, 102, 0.4);
    }
    </style>
    """, unsafe_allow_html=True)

# Gestión de archivos
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
        {"Producto": "Pastas América", "Categoría": "Pastas", "Presentación": "1kg", "Marca": "América"},
        {"Producto": "Margarina La Delicia", "Categoría": "Grasas", "Presentación": "500gr", "Marca": "La Delicia"}
    ]
    return pd.DataFrame(productos)

df_salvic = cargar_datos()

# --- 4. BARRA LATERAL (Logo solo aquí para profesionalismo) ---
with st.sidebar:
    if os.path.exists(ruta_logo):
        st.image(ruta_logo, use_container_width=True)
    st.markdown("<br>", unsafe_allow_html=True)
    menu = st.radio("Navegación Principal", ["Inicio", "Catálogo Interactivo", "Contacto"])
    st.markdown("---")
    st.caption("RIF J-29470578-2")

# --- 5. SECCIÓN: INICIO (REDiseñada) ---
if menu == "Inicio":
    # Banner de bienvenida
    st.markdown("""
        <div class="hero-section">
            <h1 style='color: #1A237E; margin:0;'>Distribuidora SALVIC C.A.</h1>
            <p style='color: #546E7A; font-size: 1.2rem;'>Comprometidos con el abastecimiento nacional.</p>
        </div>
    """, unsafe_allow_html=True)

    col_vacia, col_contenido = st.columns([1, 2])

    with col_contenido:
        # Reseña con alineación derecha
        st.markdown("""
            <div class="pro-card text-right">
                <h3 style='color: #1976D2;'>Nuestra Historia</h3>
                <p>Nacimos con el propósito firme de ser el puente más confiable entre los mejores 
                productores y el hogar venezolano. Con sede en Venezuela, hemos consolidado una red 
                capaz de llevar productos esenciales a cada rincón del país con puntualidad y excelencia.</p>
            </div>
        """, unsafe_allow_html=True)

        # Propuesta de valor con alineación derecha
        st.markdown("""
            <div class="pro-card text-right">
                <h3 style='color: #1976D2;'>Propuesta de Valor</h3>
                <p>Nuestra ventaja reside en la <b>agilidad operativa</b> y un catálogo curado que 
                equilibra calidad y costo. No solo entregamos mercancía; ofrecemos soluciones de 
                inventario para negocios que buscan estabilidad y marcas de alto impacto.</p>
            </div>
        """, unsafe_allow_html=True)

# --- 6. SECCIÓN: CATÁLOGO ---
elif menu == "Catálogo Interactivo":
    st.title("📦 Consulta de Disponibilidad")
    
    c1, c2 = st.columns([3, 1])
    with c1:
        busqueda = st.text_input("Buscar producto o marca...", placeholder="Ej: Café, Masia...")
    with c2:
        filtro_cat = st.selectbox("Filtrar por:", ["Todas"] + sorted(list(df_salvic["Categoría"].unique())))

    # Filtrado dinámico
    res = df_salvic.copy()
    if busqueda:
        res = res[res["Producto"].str.contains(busqueda, case=False) | res["Marca"].str.contains(busqueda, case=False)]
    if filtro_cat != "Todas":
        res = res[res["Categoría"] == filtro_cat]

    st.dataframe(res, use_container_width=True, hide_index=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button("Solicitar Lista de Precios vía WhatsApp", "https://wa.me/584122440691?text=Hola,%20me%20interesa%20el%20catalogo")

# --- 7. SECCIÓN: CONTACTO ---
elif menu == "Contacto":
    st.title("📬 Contacto")
    col1, col2 = st.columns(2)
    with col1:
        st.info("📍 **Operaciones Nacionales** | Envíos garantizados.")
        st.write("📞 **Teléfono:** 0412-2440691")
        st.write("✉️ **Email:** salvicdistribuidora@gmail.com")
    with col2:
        st.success("📸 Síguenos en Instagram: [@salvicdistribuidora](https://instagram.com/salvicdistribuidora)")

st.markdown("---")
st.caption(f"© {pd.Timestamp.now().year} SALVIC C.A. | Aliados en tu crecimiento.")
