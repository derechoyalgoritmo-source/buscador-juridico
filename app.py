import streamlit as st
import google.generativeai as genai

st.title("⚖️ Prueba de Conexión")

# PROBAMOS CON LA SEGUNDA LLAVE (terminada en zqil)
API_KEY = "AIzaSyCnU1irAQzAUJoaMPaQkr935yedKx5L6OA" 
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-1.5-flash")

query = st.text_input("Escribí cualquier palabra para probar:")

if query:
    try:
        # La consulta más simple del mundo
        response = model.generate_content(f"Hola, respondé solo con la palabra 'OK' si recibís esto: {query}")
        st.success(response.text)
    except Exception as e:
        st.error(f"Error definitivo: {e}")
