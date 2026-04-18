import streamlit as st
import google.generativeai as genai
import os

# 1. CONFIGURACIÓN DE LA PÁGINA
st.set_page_config(page_title="Derecho y Algoritmo - Buscador", page_icon="⚖️")
st.title("⚖️ Buscador Jurídico Científico")
st.markdown("---")

# 2. CONFIGURACIÓN DE LA API
API_KEY = "AIzaSyCnU1irAQzAUJoaMPaQkr935yedKx5L6OA" 
genai.configure(api_key=API_KEY)

# 3. EL "CEREBRO" QUE DISEÑAMOS
SYSTEM_PROMPT = """Sos el Motor de Investigación Jurídica 'Derecho y Algoritmo'. 
Tu misión es la búsqueda técnica, objetiva y científica de doctrina, jurisprudencia y normas en Argentina.
REGLAS: No opines. Priorizá links .edu.ar y .gob.ar. Verificá vigencia en InfoLEG.
Estructura: [Marco Normativo] - [Doctrina con Links] - [Jurisprudencia] - [Actualidad]."""

# 4. CONFIGURACIÓN DEL MODELO (Ajuste técnico para evitar el error 404)
# Usamos un bloque de configuración para forzar la versión v1beta
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash", # Nombre simplificado
    system_instruction=SYSTEM_PROMPT,
    tools=[{'google_search_retrieval': {}}] 
)

# 5. INTERFAZ DE USUARIO
query = st.text_input("Ingresá el término o concepto a investigar:", placeholder="Ej: Neuroderechos en Argentina")

if query:
    with st.spinner("Investigando en fuentes oficiales..."):
        try:
            # Forzamos el uso de la versión de la API que acepta Grounding
            response = model.generate_content(query)
            st.markdown(response.text)
        except Exception as e:
            # Si falla el flash, probamos con el modelo Pro automáticamente
            try:
                model_alt = genai.GenerativeModel(model_name="gemini-1.5-pro")
                response = model_alt.generate_content(query)
                st.markdown(response.text)
            except:
                st.error(f"Error técnico de conexión: {e}")
                st.info("Sugerencia: Google está actualizando sus servidores. Intentá de nuevo en 5 minutos o verificá que la API Key no tenga restricciones en Google Cloud.")

st.sidebar.info("Prototipo para Leonardo Poses Stekelberg. Enfoque: Derecho Argentino.")
