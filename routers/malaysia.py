from fastapi import APIRouter, HTTPException
from schema.malaysia import XValues
import joblib
import os
from sklearn.preprocessing import StandardScaler


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


scaler = load_scaler(r"\models\malaysia\malayasia_scaler.joblib")

model = load_model(r"\models\malaysia\Malaysian_House_Price_model.joblib")



router = APIRouter(prefix='/malaysia', tags=['malaysia House Price Predicition'])

@router.post("/predict")
def predict_price(values: XValues):
    if scaler == None:
        raise HTTPException(detail={"Internal Server Error":'scaler file not Found'}, status_code=404) 
    elif model == None:
        raise HTTPException(detail={"Internal Server Error": 'model not Found'}, status_code=404) 
    else:
        price = model.predict(scaler.transform(values.get()))[0]
        return {"price": price, "Currency":"Malaysian Ringgits"}