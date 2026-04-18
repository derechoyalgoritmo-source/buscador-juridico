import streamlit as st
import google.generativeai as genai

# CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Derecho y Algoritmo", page_icon="⚖️")
st.title("⚖️ Buscador Jurídico Científico")

# CONFIGURACIÓN DE LA API (Clave activa confirmada)
API_KEY = "AIzaSyCnU1irAQzAUJoaMPaQkr935yedKx5L6OA" 
genai.configure(api_key=API_KEY)

# SYSTEM PROMPT
SYSTEM_PROMPT = """Sos un investigador jurídico experto en Derecho Argentino. 
Tu objetivo es proveer normativa, doctrina y jurisprudencia de fuentes oficiales (.gob.ar, .edu.ar, InfoLEG). 
No des consejos legales, solo información técnica."""

# CONFIGURACIÓN DEL MODELO CON SALVAGUARDAS
@st.cache_resource
def load_model():
    # Intentamos configurar el buscador con la herramienta de Google
    return genai.GenerativeModel(
        model_name="gemini-1.5-flash",
        system_instruction=SYSTEM_PROMPT,
        tools=[{'google_search_retrieval': {}}]
    )

model = load_model()

# INTERFAZ
query = st.text_input("Investigación técnica sobre:", placeholder="Ej: Ley de Riesgos del Trabajo")

if query:
    with st.spinner("Buscando en repositorios científicos..."):
        try:
            # Prueba de ejecución estándar
            response = model.generate_content(query)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Aviso de conexión: {e}")
            st.info("Intentando búsqueda alternativa sin filtros de búsqueda externa...")
            # Si falla el grounding, responde con el conocimiento base para no dejarte vacío
            model_basic = genai.GenerativeModel("gemini-1.5-flash")
            response_alt = model_basic.generate_content(f"Basado en derecho argentino: {query}")
            st.markdown(response_alt.text)
