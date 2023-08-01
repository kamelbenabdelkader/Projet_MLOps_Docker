import streamlit as st
import requests
from datetime import datetime
import pandas as pd
import pickle
from PIL import Image
import time



# Fonction qui charge le fichier css
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")




# Appel à l'API pour récupérer les informations de vol
url = "https://mlopskamschems.azurewebsites.net/"
response = requests.get(url)
flights = response.json()
url1 = "https://mlopskamschems.azurewebsites.net/predict"




# Fonction pour la page "Ajouter"
def add_page():


    st.title("Formulaire d'entrée pour les mesures d'une fleur")

    # Créer des widgets pour les mesures de la fleur
    sepal_length = st.number_input("Longueur du sépale", value=5.7, step=0.1)
    sepal_width = st.number_input("Largeur du sépale", value=3.1, step=0.1)
    petal_length = st.number_input("Longueur du pétale", value=4.9, step=0.1)
    petal_width = st.number_input("Largeur du pétale", value=2.2, step=0.1)

    # Afficher les mesures de la fleur
    st.write("Mesures de la fleur:")
    st.write(f"Longueur du sépale: {sepal_length}")
    st.write(f"Largeur du sépale: {sepal_width}")
    st.write(f"Longueur du pétale: {petal_length}")
    st.write(f"Largeur du pétale: {petal_width}")
    st.title("MODEL IRIS")


    if st.button("Ajouter Fleur", key="ajouter_fleur_button"):
        iris_data = {
                "sepal_length": sepal_length ,
                "sepal_width":sepal_width,
                "petal_length":petal_length,
                "petal_width":petal_width
            }

            # Envoyer les données à l'API
        response = requests.get(url1, json=iris_data)
            # Vérifier si la requête a réussi
        if response.ok:
                with st.spinner('Wait for it...'):
                    time.sleep(2)
                st.success("Les informations de votre fleur ont été ajouté avec succès !")
                st.write(f"La fleure est : {response.json()['prediction']}.")
                st.write(f"Avec une probabilité d'exactitude de : {response.json()['probability']}.")

        else:
                st.error("Erreur lors de l'ajout des informations de votre fleur.")

# Fonction pour la page "Métriques"
def metrics_page():
    st.title("Graphes")

#---------------------  Sidebar  ----------------------#
# Menu déroulant pour sélectionner la page à afficher
menu = ["iris", "Graphes"]
choice = st.sidebar.selectbox(" ", menu)
# st.sidebar.title("IRIS")
# image = Image.open('img1.PNG')
# im = image.resize((150, 250))
# st.sidebar.image(im, caption='Sunrise by the mountains')


# Affichage de la page correspondant à la sélection du menu
if choice == "iris":
    add_page()
else:
    metrics_page()
