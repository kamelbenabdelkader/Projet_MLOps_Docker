# 1. Library imports
from app.models import IrisSpecies
from app.model import IrisModel
from fastapi import FastAPI

model = IrisModel()
app = FastAPI()

@app.get('/')
async def index():
    return {'message': 'Hello, stranger !!!'}





