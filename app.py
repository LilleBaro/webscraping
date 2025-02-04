import streamlit as st
from streamlit_option_menu import option_menu
from pages import scraping, analyse, dashboard, evaluation

# Configuration de la page
st.set_page_config(page_title="Scraping et Analyse", layout="wide")

# Supprimer la sidebar
st.markdown("""
    <style>
        [data-testid="stSidebar"] {display: none;}
    </style>
""", unsafe_allow_html=True)

# 📌 Barre de navigation
selected = option_menu( 
    menu_title="M E N U", 
    options=["Accueil", "Scraping", "Vue des données non-traitées", "Dashboard", "Evaluation"],
    icons=["house", "cloud-download", "table", "bar-chart", "stars"],
    menu_icon="cast",  
    default_index=0,  
    orientation="horizontal", 
    styles={
        "container": {"padding": "0!important", "background-color": "#F0F2D6"},  
        "icon": {"color": "#191970", "font-size": "20px"},  
        "nav-link": {"font-size": "16px", "text-align": "center", "margin": "0px", "--hover-color": "#E1AD01"},
        "nav-link-selected": {"background-color": "#E1AD01"},  
                },
    ) 

if selected == "Accueil":
    st.title("📊 Scraping & Analyse des Annonces Immobilières")
    
    st.write("""
    Bienvenue dans votre application de scraping et d'analyse des annonces immobilières 📌  
    Cet outil vous permet de **récupérer, visualiser et analyser les annonces immobilières** disponibles sur Expat-Dakar.  
    """)
    
    st.subheader("🚀 Fonctionnalités disponibles :")
    st.markdown("""
    - **📥 Scraping** : Récupérez les annonces immobilières en quelques clics.
    - **📊 Vue des données non-traitées** : Explorez les annonces brutes collectées.
    - **📈 Dashboard interactif** : Analysez les tendances du marché avec des statistiques et des graphiques interactifs.
    """)

    st.subheader("📌 Comment utiliser l'application ?")
    st.markdown("""
    1. **Allez dans la section "Scraping"** et sélectionnez la catégorie que vous voulez récupérer.
    2. **Lancez le scraping** pour récupérer les données en temps réel.
    3. **Visualisez les données brutes** dans la section "Vue des données non-traitées".
    4. **Analysez les tendances** dans le "Dashboard" interactif.
    """)

    st.info("⚡ Conseil : Pour une meilleure expérience, utilisez un écran large et testez différentes catégories !")

    st.write("📌 **Développé avec Ibrahima Sory pour simplifier l'analyse immobilière**")

elif selected == "Scraping":
    scraping.show_scraping_page()

elif selected == "Vue des données non-traitées":
    analyse.show_analysis_page()

elif selected == "Dashboard":
    dashboard.show_dashboard()

elif selected == "Evaluation":
    evaluation.show_evaluation_page()
