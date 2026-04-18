import streamlit as st
import google.generativeai as genai

# 1. Configuracion de la pagina
st.set_page_config(page_title="Derecho y Algoritmo", page_icon="⚖️")
st.title("⚖️ Buscador Jurídico Científico")

# 2. Configuracion de la API
API_KEY = "AIzaSyCnU1irAQzAUJoaMPaQkr935yedKx5L6OA" 
genai.configure(api_key=API_KEY)

# 3. Instrucciones
SYSTEM_PROMPT = """Sos el Motor de Investigación Jurídica 'Derecho y Algoritmo'. 
Tu misión es la búsqueda técnica de doctrina, jurisprudencia y normas en Argentina."""

# 4. Modelo
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    system_instruction=SYSTEM_PROMPT
)

# 5. Interfaz
query = st.text_input("Investigación técnica sobre:", placeholder="Ej: Trabajo no registrado")

if query:
    with st.spinner("Buscando..."):
        try:
            response = model.generate_content(query)
            st.markdown(response.text)
        except Exception as e:
            st.error(f"Error: {e}")
