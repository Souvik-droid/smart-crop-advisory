import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import joblib

# Load data
df = pd.read_csv("crop_data.csv")

X = df.drop("label", axis=1)
y = df["label"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "app/models/crop_model.pkl")

print("Model trained successfully!")