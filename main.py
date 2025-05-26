from fastapi import FastAPI
import numpy as np
import joblib
from pydantic import BaseModel

# Load model yang sudah disimpan
model = joblib.load(r'D:\Pemrograman\machine learning\portfolio\house-predict\house-predict-project.pkl')

app = FastAPI()

# Model untuk input data
class HouseData(BaseModel):
    bedrooms: int
    bathrooms: int
    sqft_lot: int
    floors: int
    yr_built: int

@app.post("/predict")
def predict_price(data: HouseData):
    # Mengambil data dari request body dan mengubah menjadi numpy array
    input_data = np.array([[data.bedrooms, data.bathrooms, data.sqft_lot, data.floors, data.yr_built]])
    
    # Prediksi harga
    harga_rumah = model.predict(input_data)[0]
    
    # Mengembalikan harga prediksi dalam format JSON
    return {"predicted_price": f"${harga_rumah:,.2f}"}

# uvicorn main:app --reload
# http://localhost:8000/predict
