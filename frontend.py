import streamlit as st
import requests

st.title("🌾 Smart Crop Advisory System")

st.header("Enter Soil Details")

nitrogen = st.number_input("Nitrogen")
phosphorus = st.number_input("Phosphorus")
potassium = st.number_input("Potassium")
temperature = st.number_input("Temperature")
humidity = st.number_input("Humidity")
ph = st.number_input("pH")
rainfall = st.number_input("Rainfall")
city = st.text_input("City")

st.header("Upload Leaf Image")
image = st.file_uploader("Choose an image", type=["jpg", "png"])

if st.button("Get Advisory"):

    if image is None:
        st.error("Please upload an image")
    elif city == "":
        st.error("Please enter city")
    else:
        try:
            # ✅ Correct file format
            files = {
                "file": (image.name, image.getvalue(), image.type)
            }

            # ✅ Send request
            response = requests.post(
                "http://127.0.0.1:8000/smart/advisory",
                data={
                    "nitrogen": nitrogen,
                    "phosphorus": phosphorus,
                    "potassium": potassium,
                    "temperature": temperature,
                    "humidity": humidity,
                    "ph": ph,
                    "rainfall": rainfall,
                    "city": city
                },
                files=files
            )

            if response.status_code == 200:
                result = response.json()

                st.subheader("🌱 Crop Recommendation")
                st.write(result["crop_recommendation"])

                st.subheader("🌦 Weather")
                st.write(result["weather"])

                st.subheader("🐛 Disease Detected")
                st.write(result["disease_detected"])

                st.subheader("📋 Crop Advisory")
                for adv in result["crop_advisory"]:
                    st.write("- " + adv)

                st.subheader("💊 Disease Advisory")
                st.write(result["disease_advisory"])

            else:
                st.error("Backend error: " + str(response.status_code))

        except Exception as e:
            st.error(f"Error: {e}")