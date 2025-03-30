from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import india, america, malaysia


app = FastAPI(title='House Price Prediction')

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(india.router)
app.include_router(america.router)
app.include_router(malaysia.router)

@app.get('/')
def HomeSage():
    return {"message": "Welcome to HomeSage House Price Prediction API"}