from fastapi import APIRouter, HTTPException
from schema.india import XValues
from sklearn.preprocessing import StandardScaler
import joblib
import os
import json


with open(os.getcwd() + r"/data/india/valid_state_city.json", "r") as file:
    STATE_CITY_MAPPING = json.load(file)


def load_scaler(file_loaction) -> StandardScaler | None:
    try:
        return joblib.load(os.getcwd() + file_loaction)
    except FileNotFoundError:
        return None
    
def load_model(file_loaction):
    try:
        return joblib.load(os.getcwd() + file_loaction)
    except FileNotFoundError:
        return None

  
scaler = load_scaler(r"\models\india\IndianInputScaler.joblib")

model = load_model(r"\models\india\Indian_House_Price_model.joblib")





router = APIRouter(prefix='/india', tags=['India House Price Predicition'])

@router.post("/predict")
def predict_price(value: XValues):
    if scaler == None:
        raise HTTPException(detail={"Internal Server Error":'scaler file not Found'}, status_code=404) 
    elif model == None:
        raise HTTPException(detail={"Internal Server Error": 'model not Found'}, status_code=404)
    
    elif value.location_status() == False:
        raise HTTPException(detail={"Invalid Request": "Invalid state or city"}, status_code=400)
    
    else: 

        price = model.predict(scaler.transform(value.get()))[0] * 100000

        return {"price":price, "Currency":"Rupee" }
        

