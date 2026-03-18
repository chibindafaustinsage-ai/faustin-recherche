import streamlit as st
import google.generativeai as genai

# Nom de l'application de Faustin
st.set_page_config(page_title="FAUSTIN CHIBINDA SAGE Recherche", page_icon="🔬")

# Ta clé API
genai.configure(api_key="AIzaSyCQwvTsRWzj9BP5IcKCqibs5PTK2rWK-uQ")
model = genai.GenerativeModel('gemini-1.5-flash')

st.title("🔬 FAUSTIN CHIBINDA SAGE Recherche")
st.write("Bienvenue sur mon application de recherche IA.")

sujet = st.text_input("Que voulez-vous explorer aujourd'hui ?")

if st.button("Lancer la recherche 🚀"):
    if sujet:
        with st.spinner("Recherche en cours..."):
            reponse = model.generate_content(f"Fais un rapport scientifique sur {sujet}")
            st.markdown(reponse.text)
            st.image(f"https://pollinations.ai/p/{sujet}?width=1024")
