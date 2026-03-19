import streamlit as st
from google import genai

# Configuration de la page
st.set_page_config(page_title="Chibinda Sage Recherche", page_icon="🚀")

# Connexion au client Google GenAI
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
                response = client.models.generate_content(
                    model="gemini-2.0-flash", 
                    contents=prompt
                )
                st.markdown("### Résultat :")
                st.write(response.text)
        except Exception as e:
            st.error(f"Erreur : {e}")
    else:
        st.warning("bonjour mon ami (e) .")

# --- SECTION SOUTIEN ET REMERCIEMENTS ---
st.markdown("---") # Une ligne de séparation
st.subheader("🙏 Remerciements & Soutien")
st.write("Merci d'utiliser mon application de recherche ! Si ce service vous est utile et que vous souhaitez m'encourager à l'améliorer, vous pouvez me soutenir.")

# Encadré pour le numéro de téléphone
st.info("💎 **Pour me soutenir (Airtime / M-Pesa / Airtel Money) :** \n\n **+243 [813397457, 986265221]**")

st.caption("© 2026 - Créé par Chibinda Faustin Sage")
