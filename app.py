import streamlit as st
import google.generativeai as genai

# Configuration de la page
st.set_page_config(page_title="Chibinda Sage Recherche", layout="centered")

# Récupération de la clé API depuis les Secrets de Streamlit
try:
    genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("La clé API est manquante dans les Secrets de Streamlit.")

st.title("CHIBINDA SAGE Recherche")
st.write("Bienvenue sur mon application de recherche IA.")

# Zone de saisie
prompt = st.text_input("Que voulez-vous explorer aujourd'hui ?", placeholder="Ex: Quels sont les bienfaits de la technologie ?")

if st.button("Lancer la recherche 🚀"):
    if prompt:
        try:
            # LE MODÈLE CORRECT EST ICI
            model = genai.GenerativeModel('gemini-1.5-flash')
            
            with st.spinner("Recherche en cours..."):
                response = model.generate_content(prompt)
                st.markdown("### Résultat :")
                st.write(response.text)
        except Exception as e:
            st.error(f"Une erreur est survenue : {e}")
    else:
        st.warning("Veuillez entrer une question.")
