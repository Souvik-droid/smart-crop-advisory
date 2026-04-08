from fastapi import FastAPI
from app.routes.smart import router as smart_router
from app.routes.crop import router as crop_router
from app.routes.weather import router as weather_router
from app.routes.disease import router as disease_router

app = FastAPI()

app.include_router(crop_router, prefix="/crop")
app.include_router(weather_router, prefix="/weather")
app.include_router(disease_router, prefix="/disease")
app.include_router(smart_router, prefix="/smart", tags=["Smart Advisory"])

@app.get("/")
def home():
    return {"message": "Running"}