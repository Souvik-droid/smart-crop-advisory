from fastapi import APIRouter, UploadFile, File
import shutil

from app.services.disease_service import predict_disease
from app.utils.decision_engine import disease_advisory

router = APIRouter()

@router.post("/detect")
async def detect_disease(file: UploadFile = File(...)):
    file_path = f"temp_{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    disease = predict_disease(file_path)
    advisory = disease_advisory(disease)

    return {
        "disease": disease,
        "advisory": advisory
    }