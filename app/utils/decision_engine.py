# EXISTING FUNCTION (keep this)
def generate_advisory(crop, weather):
    advice = []

    if weather["rainfall"] > 100:
        advice.append("High rainfall expected. Avoid irrigation.")
    else:
        advice.append("Low rainfall. Irrigation recommended.")

    if weather["temperature"] > 35:
        advice.append("High temperature. Monitor crop stress.")

    if crop == "rice":
        advice.append("Maintain water level.")
    elif crop == "wheat":
        advice.append("Avoid excess water.")
    elif crop == "maize":
        advice.append("Avoid waterlogging.")

    return advice


# 🔥 ADD THIS FUNCTION (IMPORTANT)
def disease_advisory(disease):
    advisory_db = {
        "Early_blight": {
            "cause": "Fungal infection due to high humidity",
            "treatment": "Spray Mancozeb or Chlorothalonil",
            "prevention": "Avoid overhead irrigation"
        },
        "Late_blight": {
            "cause": "Cool and moist conditions",
            "treatment": "Apply Metalaxyl fungicide",
            "prevention": "Remove infected leaves"
        },
        "Healthy": {
            "cause": "No disease",
            "treatment": "No action needed",
            "prevention": "Maintain crop care"
        }
    }

    return advisory_db.get(disease, {
        "cause": "Unknown",
        "treatment": "Consult expert",
        "prevention": "Monitor regularly"
    })