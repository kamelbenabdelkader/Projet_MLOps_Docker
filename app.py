# 1. Library imports
import uvicorn
from typing import List
from models import IrisSpecies ,  Prediction
from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from urllib.parse import urlparse
from dotenv import load_dotenv
import os
import pickle
import pandas as pd
from Model import IrisModel
import pymysql

# Charger les variables d'environnement à partir du fichier .env
load_dotenv()

app = FastAPI()
model = IrisModel()



def connect():
    # Récupérer l'URL de la base de données à partir des variables d'environnement
    database_url = os.getenv("DATABASE_URL")

    # Extraire les composants de l'URL de la base de données
    url_components = urlparse(database_url)
    db_host = url_components.hostname
    db_user = url_components.username
    db_password = url_components.password
    db_name = url_components.path.strip('/')

    # Configurer la connexion à la base de données MySQL
    conn = pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name
    )
    return conn

# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, WORLD'}


# 5. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted flower species with the confidence
@app.get('/predict')
def predict_species(iris: IrisSpecies):
    data = iris.dict()
    prediction, probability = model.predict_species(
        data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width']
    )
    return {
        'prediction': prediction,
        'probability': probability
    }



@app.post("/add")
async def create_item(item:  Prediction):
    # Perform operations on the database
    conn = connect()
    with conn.cursor() as cursor:
        query = "INSERT INTO prediction (prediction, probability) " \
                 "VALUES (%s, %s)"
        values = (item.prediction, item.probability)
        cursor.execute(query, values)
        conn.commit()

# 4. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
