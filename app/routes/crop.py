from fastapi import APIRouter
from pydantic import BaseModel

from app.services.crop_service import predict_crop
from app.services.weather_service import get_weather_data
from app.utils.decision_engine import generate_advisory

router = APIRouter()

class CropInput(BaseModel):
    nitrogen: float
    phosphorus: float
    potassium: float
    temperature: float
    humidity: float
    ph: float
    rainfall: float

@router.post("/recommend")
def recommend_crop(data: CropInput):
    crop = predict_crop(data)
    weather = get_weather_data("Delhi")
    advisory = generate_advisory(crop, weather)

    return {
        "recommended_crop": crop,
        "weather": weather,
        "advisory": advisory
    }