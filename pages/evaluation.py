import streamlit as st
import smtplib
from email.message import EmailMessage

# 📌 Récupération des informations depuis Streamlit Secrets
EMAIL_SENDER = "iss654864@gmail.com"
EMAIL_PASSWORD = "fjxhsladuowjkygl"
EMAIL_RECEIVER = "ibrahimasorysane986@gmail.com"

def send_email(user_email, rating, comment):
    """ Envoie un e-mail avec l'évaluation """
    try:
        msg = EmailMessage()
        msg.set_content(f"""
        📌 Nouvelle évaluation de l'application
        
        ⭐ Note donnée : {rating}
        💬 Commentaire : {comment}
        ✉️ Adresse e-mail de l'utilisateur : {user_email}
        """)

        msg["Subject"] = "Nouvelle Évaluation de l'application"
        msg["From"] = EMAIL_SENDER
        msg["To"] = EMAIL_RECEIVER

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_SENDER, EMAIL_PASSWORD)
            server.send_message(msg)

        return True
    except Exception as e:
        st.error(f"Erreur lors de l'envoi : {e}")
        return False

def show_evaluation_page():
    """ Affiche la page d'évaluation de l'application """
    st.title("⭐ Évaluez notre Application !")

    st.write("Donnez-nous votre avis pour améliorer l'expérience utilisateur !")

    # 📌 Formulaire d'évaluation
    #sentiment_mapping = ["1 étoiles", "2 étoiles", "3 étoiles", "4 étoiles", "5 étoiles"]
    user_email = st.text_input("📧 Votre adresse e-mail", "")
    rating = st.feedback("stars")
    comment = st.text_area("💬 Votre message", "")

    if st.button("✅ Envoyer l'évaluation"):
        if user_email and comment:
            success = send_email(user_email, rating, comment)
            if success:
                st.success("Merci pour votre évaluation ! Votre message a été envoyé.")
            else:
                st.error("Une erreur est survenue lors de l'envoi du message. Réessayez plus tard.")
        else:
            st.warning("Veuillez remplir tous les champs.")
