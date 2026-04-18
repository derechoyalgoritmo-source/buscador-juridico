import streamlit as st
import google.generativeai as genai

# 1. Configuración de la página
st.set_page_config(page_title="Derecho y Algoritmo", page_icon="⚖️")
st.title("⚖️ Buscador Jurídico Científico")

# 2. Configuración de la API
API_KEY = "AIzaSyCnU1irAQzAUJoaMPaQkr935yedKx5L6OA" 
genai.configure(api_key=API_KEY)

# 3. Instrucciones del Sistema (Tu filtro científico)
SYSTEM_PROMPT = """Sos el Motor de Investigación Jurídica 'Derecho y Algoritmo'. 
Tu misión es la búsqueda técnica de doctrina, jurisprudencia y normas en Argentina.
REGLAS: No opines. Priorizá links .edu.ar y .gob.ar. 
Estructura: [Marco Normativo] - [Doctrina] - [Jurisprudencia] - [Actualidad]."""

# 4. Carga del Modelo (Versión Estable)
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

# 5. Interfaz
query = st.text_input("Investigación técnica sobre:", placeholder="Ej: Trabajo no registrado")

if query:
    with st.spinner("Buscando en repositorios..."):
        try:
            # Consulta directa
            response = model.generate_content(query)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Hubo un problema con la consulta: {e}")
            st.info("Sugerencia: Revisá si la API Key en Google AI Studio tiene restricciones de uso.")

st.sidebar.info("Prototipo de Leonardo Poses Stekelberg. Enfoque: Derecho argentino.")
