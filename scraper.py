import requests
from bs4 import BeautifulSoup
import pandas as pd

URLS = {
    "Appartements à louer": "https://www.expat-dakar.com/appartements-a-louer",
    "Appartements meublés": "https://www.expat-dakar.com/appartements-meubles",
    "Terrains à vendre": "https://www.expat-dakar.com/terrains-a-vendre"
}

try:
    response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
    st.write(f"🔍 Statut de la requête : {response.status_code}")
    st.write("🔹 Aperçu du contenu :", response.text[:500])  # Afficher les 500 premiers caractères
except Exception as e:
    st.error(f"Erreur lors de la requête : {e}")

def scrape_expat_dakar(url, max_pages=5):
    all_data = []

    for page in range(1, max_pages + 1):
        page_url = f"{url}?page={page}"
        response = requests.get(page_url)

        if response.status_code != 200:
            continue

        soup = BeautifulSoup(response.text, "html.parser")
        listings = soup.find_all("div", class_="listings-cards__list-item")

        for listing in listings:
            title = listing.find("div", class_="listing-card__header__title")
            details = title.text.strip() if title else "N/A"

            tags = listing.find("div", class_="listing-card__header__tags")
            tags_text = tags.text.strip() if tags else "N/A"

            loc = listing.find("div", class_="listing-card__header__location")
            adresse = loc.text.strip() if loc else "N/A"

            price = listing.find("span", class_="listing-card__price__value")
            prix = price.text.strip() if price else "N/A"

            image_tag = listing.find("img")
            image_link = image_tag["src"] if (image_tag and image_tag.has_attr("src")) else "N/A"

            all_data.append([details, tags_text, adresse, prix, image_link])

    return pd.DataFrame(all_data, columns=["Détails", "Tags", "Adresse", "Prix", "Image"])
