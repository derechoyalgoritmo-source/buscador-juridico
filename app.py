import streamlit as st
import google.generativeai as genai

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Derecho y Algoritmo - Buscador", page_icon="⚖️")
st.title("⚖️ Buscador Jurídico Científico")
st.markdown("---")

# CONFIGURACIÓN DE LA API (Aquí pondrás tu clave)
API_KEY = "AIzaSyCnU1irAQzAUJoaMPaQkr935yedKx5L6OA" 
genai.configure(api_key=API_KEY)

# EL "CEREBRO" QUE DISEÑAMOS
SYSTEM_PROMPT = """Sos el Motor de Investigación Jurídica 'Derecho y Algoritmo'. 
Tu misión es la búsqueda técnica, objetiva y científica de doctrina, jurisprudencia y normas en Argentina.
REGLAS: No opines. Priorizá links .edu.ar y .gob.ar. Verificá vigencia en InfoLEG.
Estructura: [Marco Normativo] - [Doctrina con Links] - [Jurisprudencia] - [Actualidad]."""

model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT,
    tools=[{'google_search_retrieval': {}}] # Activa el buscador de Google
)

# INTERFAZ DE USUARIO
query = st.text_input("Ingresá el término o concepto a investigar:", placeholder="Ej: Responsabilidad algorítmica")

if query:
    with st.spinner("Investigando en fuentes oficiales..."):
        try:
            response = model.generate_content(query)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")

st.sidebar.info("Prototipo para Leonardo Poses Stekelberg. Enfoque: Derecho Argentino.")
