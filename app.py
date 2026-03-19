import streamlit as st
from google import genai

# Configuration de la page
st.set_page_config(page_title="Chibinda Sage Recherche")

# Connexion au nouveau client Google GenAI
try:
    client = genai.Client(api_key=st.secrets["GOOGLE_API_KEY"])
except Exception as e:
    st.error("Vérifiez votre clé API dans les Secrets Streamlit.")

st.title("CHIBINDA SAGE Recherche")
st.write("Votre assistant de recherche intelligent est prêt.")

# Zone de saisie
prompt = st.text_input("Posez votre question ici :", placeholder="Ex: Quelle est l'importance de l'éducation ?")

if st.button("Lancer la recherche 🚀"):
    if prompt:
        try:
            with st.spinner("L'IA réfléchit..."):
                # Utilisation du modèle 2.0 Flash (le plus rapide au monde)
                response = client.models.generate_content(
                    model="gemini-2.0-flash", 
                    contents=prompt
                )
                st.markdown("### Résultat :")
                st.write(response.text)
        except Exception as e:
            st.error(f"Erreur lors de la génération : {e}")
    else:
        st.warning("Veuillez écrire quelque chose.")
