import joblib
import numpy as np

model = joblib.load("app/models/crop_model.pkl")

def predict_crop(data):
    features = np.array([[
        data.nitrogen,
        data.phosphorus,
        data.potassium,
        data.temperature,
        data.humidity,
        data.ph,
        data.rainfall
    ]])

    prediction = model.predict(features)
    return prediction[0]