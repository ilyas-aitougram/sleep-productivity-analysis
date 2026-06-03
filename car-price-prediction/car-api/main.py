from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class CarData(BaseModel):
    age: int
    km: int
    power: int
    brand_score: int

@app.get("/")
def home():
    return {"message": "Bienvenue sur mon API Python"}

@app.get("/health")
def health():
    return {"status": "API OK"}

@app.post("/predict")
def predict(car: CarData):
    price = 25000 - car.age * 1800 - car.km * 0.08 + car.power * 90 + car.brand_score * 700

    if price < 1000:
        price = 1000

    return {
        "estimated_price": round(price, 2)
    }