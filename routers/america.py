from fastapi import APIRouter, HTTPException
from schema.america import XValues
import numpy as np
import joblib
import asyncio


def load_model(file_loaction):
    try:
        return joblib.load(file_loaction)
    except FileNotFoundError:
        return None

model = load_model("models/america/American_House_Price_model.joblib")

router = APIRouter(prefix='/america', tags=['USA House Price Predicition'])

@router.post("/predict")
async def predict_price(values:XValues):
    if model == None:
        raise HTTPException(detail={"Internal Server Error": 'Model not Found'}, status_code=404)
    else:
        def compute_price():
            return np.expm1(model.predict(np.log1p(values.get())))[0]

        price = await asyncio.to_thread(compute_price)
        return {"price": price, "Currency": "USD"}
