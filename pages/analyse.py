import streamlit as st
from utils.data_handler import load_data

def show_analysis_page():
    st.title("📈 Analyse des données")

    # ✅ Expander pour expliquer l'utilisation de la page
    with st.expander("ℹ️ À propos de cette page"):
        st.write("""
        Cette page permet d'afficher et d'explorer les **données récupérées via le web scraping**.  
        Vous pouvez ici **visualiser les annonces collectées** avant leur traitement.
        
        **📌 Comment utiliser cette page ?**
        1. **Sélectionnez un dataset** parmi les données scrapées.
        2. **Cliquez sur "Charger les données"** pour voir les informations collectées.
        3. **Visualisez les données sous forme de tableau**.
        
        """)

    dataset_choice = st.selectbox("Sélectionnez un dataset", ["Appartements à louer non prétraité", "Appartements meublés non prétraité", "Terrains à vendre non prétraité"])

    if st.button("Charger les données"):
        df = load_data(dataset_choice)
        if df is not None:
            st.success(f"{len(df)} lignes chargées.")
            st.dataframe(df)
        else:
            st.warning("Fichier introuvable. Veuillez scraper les données d'abord.")
