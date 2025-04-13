from fastapi import APIRouter, HTTPException
from schema.india import XValues
from sklearn.preprocessing import StandardScaler
import joblib
import json
import asyncio


with open("data/india/valid_state_city.json", "r") as file:
    STATE_CITY_MAPPING = json.load(file)


def load_scaler(file_loaction) -> StandardScaler | None:
    try:
        return joblib.load(file_loaction)
    except FileNotFoundError:
        return None
    
def load_model(file_loaction):
    try:
        return joblib.load(file_loaction)
    except FileNotFoundError:
        return None

  
scaler = load_scaler("models/india/IndianInputScaler.joblib")

model = load_model("models/india/Indian_House_Price_model.joblib")





router = APIRouter(prefix='/india', tags=['India House Price Predicition'])

@router.post("/predict")
async def predict_price(value: XValues):
    if scaler == None:
        raise HTTPException(detail={"Internal Server Error":'scaler file not Found'}, status_code=404) 
    elif model == None:
        raise HTTPException(detail={"Internal Server Error": 'model not Found'}, status_code=404)
    
    elif value.location_status() == False:
        raise HTTPException(detail={"Invalid Request": "Invalid state or city"}, status_code=400)
    
    else: 
        def compute_price():
            transformed = scaler.transform(value.get())
            return model.predict(transformed)[0] * 100000

        price = await asyncio.to_thread(compute_price)
        return {"price": price, "Currency": "Rupee"}
        

