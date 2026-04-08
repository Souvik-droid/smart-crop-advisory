from fastapi import APIRouter, UploadFile, File, Form
import shutil

from app.services.crop_service import predict_crop
from app.services.weather_service import get_weather_data
from app.services.disease_service import predict_disease
from app.utils.decision_engine import generate_advisory, disease_advisory

router = APIRouter()

@router.post("/advisory")
async def smart_advisory(
    nitrogen: float = Form(...),
    phosphorus: float = Form(...),
    potassium: float = Form(...),
    temperature: float = Form(...),
    humidity: float = Form(...),
    ph: float = Form(...),
    rainfall: float = Form(...),
    city: str = Form(...),
    file: UploadFile = File(...)
):

    # Save image
    file_path = f"temp_{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    # Prepare input object manually
    class InputData:
        def __init__(self):
            self.nitrogen = nitrogen
            self.phosphorus = phosphorus
            self.potassium = potassium
            self.temperature = temperature
            self.humidity = humidity
            self.ph = ph
            self.rainfall = rainfall

    data = InputData()

    # ML + Logic
    crop = predict_crop(data)
    weather = get_weather_data(city)
    disease = predict_disease(file_path)

    crop_advice = generate_advisory(crop, weather)
    disease_info = disease_advisory(disease)

    return {
        "crop_recommendation": crop,
        "weather": weather,
        "disease_detected": disease,
        "crop_advisory": crop_advice,
        "disease_advisory": disease_info
    }