import streamlit as st
import joblib
import numpy as np

# Load trained model
model = joblib.load("crop_model.pkl")

# Display an image at the top
st.image("https://images.unsplash.com/photo-1511735643442-503bb3bd348a?fm=jpg&q=60&w=3000&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MTB8fGNyb3BzfGVufDB8fDB8fHww", caption="🌾 Crop Recommendation System",  use_container_width =True)

# Define the function to make a prediction
def predict_crop(N, P, K, temperature, humidity, ph, rainfall):
    features = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
    prediction = model.predict(features)[0]
    return prediction

# Streamlit UI
st.title("🌾 Crop Recommendation System")

st.markdown("Provide the soil and weather conditions to get a crop recommendation.")

# Input fields
N = st.number_input("Nitrogen (N)", min_value=0, max_value=140, step=1)
P = st.number_input("Phosphorus (P)", min_value=0, max_value=140, step=1)
K = st.number_input("Potassium (K)", min_value=0, max_value=200, step=1)
temperature = st.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, step=0.1)
humidity = st.number_input("Humidity (%)", min_value=0.0, max_value=100.0, step=0.1)
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.1)
rainfall = st.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, step=0.1)

# Prediction button
if st.button("Predict Crop"):
    predicted_crop = predict_crop(N, P, K, temperature, humidity, ph, rainfall)
    st.success(f"Recommended Crop: {predicted_crop}")

#streamlit run crop_recommendation_app.py(to-run)