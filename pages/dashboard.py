import streamlit as st
import plotly.express as px
import pandas as pd
from utils.data_handler import load_data

def show_dashboard():
    st.title("📊 Tableau de Bord")

    # ✅ Expander pour expliquer l'utilisation de la page
    with st.expander("ℹ️ À propos de cette page"):
        st.write("""
        Cette page permet de **visualiser et analyser** les données immobilières collectées et prétraitées via le web scraping avec beautifull soap.
        
        **📌 Fonctionnalités disponibles :**
        - **📋 Aperçu des données** : Affiche les annonces récupérées.
        - **🎯 Filtrage interactif** : Filtrez les annonces par prix, quartier et nombre de chambres.
        - **📊 Statistiques descriptives** : Visualisez les principales statistiques du dataset.
        - **💰 Analyse des prix** : Histogramme de la distribution des prix.
        - **📈 Corrélation Prix vs Superficie** : Explorez la relation entre le prix et la superficie.

        💡 **Conseil :** Affinez les filtres pour obtenir des analyses plus pertinentes.
        """)

    dataset_choice = st.selectbox("📂 Choisissez un dataset", ["Appartements à louer", "Appartements meublés", "Terrains à vendre"])
    df = load_data(dataset_choice)

    if df is not None:
        st.write("### 📋 Aperçu des données")
        st.dataframe(df)

        # 🚨 Vérifier si la colonne "prix" existe
        if "prix" not in df.columns:
            st.error("🚨 La colonne 'prix' est introuvable dans le fichier CSV. Vérifiez le fichier.")
            st.write("Colonnes disponibles :", df.columns)
            return

        # 🎯 FILTRAGE INTERACTIF
        st.write("### 🎯 Filtrage Interactif")

        # 🏷️ Filtre par plage de prix
        if "prix" in df.columns:
            min_price, max_price = int(df["prix"].min()), int(df["prix"].max())
            price_range = st.slider("Sélectionnez une plage de prix", min_price, max_price, (min_price, max_price))
            df = df[(df["prix"] >= price_range[0]) & (df["prix"] <= price_range[1])]

        # 📍 Filtre par localisation
        if "adresse" in df.columns:
            selected_location = st.selectbox("📍 Sélectionnez un quartier", ["Tous"] + sorted(df["adresse"].unique().tolist()))
            if selected_location != "Tous":
                df = df[df["adresse"] == selected_location]

        # 🛏️ Filtre par nombre de chambres
        if "nombre_chambre" in df.columns:
            selected_rooms = st.multiselect("🛏️ Sélectionnez le nombre de chambres", sorted(df["nombre_chambre"].unique().tolist()))
            if selected_rooms:
                df = df[df["nombre_chambre"].isin(selected_rooms)]

        # 📊 Affichage des statistiques
        st.write("### 📊 Statistiques Descriptives")
        st.write(df.describe())

        # 💰 Graphique de distribution des prix
        st.write("### 💰 Répartition des prix")
        fig = px.histogram(df, x="prix", title="Distribution des prix", nbins=30)
        st.plotly_chart(fig)

        # 📈 Corrélation entre prix et Superficie
        if "superficie" in df.columns and "prix" in df.columns:
            st.write("### 📈 Corrélation entre prix et Superficie")
            fig = px.scatter(df, x="superficie", y="prix", title="Relation entre prix et Superficie", trendline="ols")
            st.plotly_chart(fig)

    else:
        st.warning("Fichier introuvable. Veuillez scraper les données d'abord.")
