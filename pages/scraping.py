import streamlit as st
import pandas as pd
from scraper import scrape_expat_dakar
from utils.data_handler import save_data

URLS = {
    "Appartements à louer": "https://www.expat-dakar.com/appartements-a-louer",
    "Appartements meublés": "https://www.expat-dakar.com/appartements-meubles",
    "Terrains à vendre": "https://www.expat-dakar.com/terrains-a-vendre"
}

def show_scraping_page():
    st.title("🔍 Scraping des annonces")

    # ✅ Expander pour expliquer l'utilisation de la page
    with st.expander("ℹ️ Comment utiliser cette page ?"):
        st.write("""
        Cette page vous permet d'extraire des annonces immobilières depuis le site Expat-Dakar.
        
        **📌 Étapes à suivre :**
        1. **Choisissez une catégorie** : Sélectionnez le type d'annonces que vous souhaitez scraper.
        2. **Définissez le nombre de pages** : Indiquez combien de pages d'annonces vous voulez récupérer.
        3. **Lancez le scraping** : Cliquez sur **"Lancer le scraping"** et patientez.
        4. **Consultez les résultats** : Une fois terminé, les annonces récupérées s'afficheront.
        5. **Téléchargez les données** : Cliquez sur **"📥 Télécharger les données"** pour exporter les annonces en format CSV.
        
        💡 **Conseil :** Plus le nombre de pages est grand, plus le scraping prendra du temps.
        """)

    category = st.selectbox("Choisissez une catégorie", list(URLS.keys()))
    max_pages = st.number_input("Nombre de pages à scraper", 1, 20, 5)

    if st.button("Lancer le scraping"):
        with st.spinner("Scraping en cours..."):
            df = scrape_expat_dakar(URLS[category], max_pages)
            #save_data(category, df)
            
            # ✅ Affichage des résultats
            st.success(f"{len(df)} annonces récupérées!")
            st.dataframe(df)

            # ✅ Bouton de téléchargement des données au format CSV
            csv = df.to_csv(index=False).encode("utf-8")
            st.download_button(
                label="📥 Télécharger les données",
                data=csv,
                file_name=f"{category.replace(' ', '_')}.csv",
                mime="text/csv"
            )
