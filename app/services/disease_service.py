import numpy as np
import os
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("app/models/disease_model/disease_model.h5")

# ✅ AUTO LOAD CLASS NAMES
DATASET_PATH = "dataset"
class_names = sorted(os.listdir(DATASET_PATH))


def predict_disease(img_path):
    img = image.load_img(img_path, target_size=(128,128))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    predictions = model.predict(img_array)
    class_index = np.argmax(predictions)

    return class_names[class_index]