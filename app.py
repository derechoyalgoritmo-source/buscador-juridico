import streamlit as st
import google.generativeai as genai

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Derecho y Algoritmo - Buscador", page_icon="⚖️")
st.title("⚖️ Buscador Jurídico Científico")
st.markdown("---")

# 2. CONFIGURACIÓN DE LA API (Corregida sin espacios ocultos)
API_KEY = "AIzaSyCnU1irAQzAUJoaMPaQkr935yedKx5L6OA" 
genai.configure(api_key=API_KEY)

# 3. EL "CEREBRO" QUE DISEÑAMOS
SYSTEM_PROMPT = """Sos el Motor de Investigación Jurídica 'Derecho y Algoritmo'. 
Tu misión es la búsqueda técnica, objetiva y científica de doctrina, jurisprudencia y normas en Argentina.
REGLAS: No opines. Priorizá links .edu.ar y .gob.ar. Verificá vigencia en InfoLEG.
Estructura: [Marco Normativo] - [Doctrina con Links] - [Jurisprudencia] - [Actualidad]."""

# 4. MODELO (Cambiado a 'gemini-1.5-flash-latest' para máxima compatibilidad)
model = genai.GenerativeModel(
    model_name="models/gemini-1.5-flash-latest",
    system_instruction=SYSTEM_PROMPT,
    tools=[{'google_search_retrieval': {}}] 
)

# 5. INTERFAZ DE USUARIO
query = st.text_input("Ingresá el término o concepto a investigar:", placeholder="Ej: Responsabilidad algorítmica")

if query:
    with st.spinner("Investigando en fuentes oficiales..."):
        try:
            # Forzamos la respuesta para evitar errores de seguridad si el tema es sensible
            response = model.generate_content(query)
            if response.text:
                st.markdown(response.text)
            else:
                st.warning("No se encontraron resultados específicos. Probá refinando los términos técnicos.")
        except Exception as e:
            st.error(f"Error técnico: {e}")
            st.info("Nota: Si el error es 404, Google está actualizando el acceso a este modelo en tu zona. Probaremos con uno alternativo si persiste.")

st.sidebar.info("Prototipo para Leonardo Poses Stekelberg. Enfoque: Derecho Argentino.")
