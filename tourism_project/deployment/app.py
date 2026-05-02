import streamlit as st
import pandas as pd
import joblib

# Load trained model
model = joblib.load("best_model.pkl")

st.title("Visit with Us - Wellness Tourism Prediction")

st.write("Enter customer details")

# Inputs
Age = st.number_input("Age", 18, 80, 30)
TypeofContact = st.selectbox("Type of Contact", ["Company Invited", "Self Enquiry"])
CityTier = st.selectbox("City Tier", [1, 2, 3])
Occupation = st.selectbox("Occupation", ["Salaried", "Small Business", "Free Lancer", "Large Business"])
Gender = st.selectbox("Gender", ["Male", "Female"])
NumberOfPersonVisiting = st.number_input("Number of Persons Visiting", 1, 10, 2)
PreferredPropertyStar = st.selectbox("Preferred Property Star", [3, 4, 5])
MaritalStatus = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
NumberOfTrips = st.number_input("Number of Trips", 0, 20, 2)
Passport = st.selectbox("Passport", [0, 1])
OwnCar = st.selectbox("Own Car", [0, 1])
NumberOfChildrenVisiting = st.number_input("Children Visiting", 0, 5, 0)
Designation = st.selectbox("Designation", ["Executive", "Manager", "Senior Manager", "VP", "AVP"])
MonthlyIncome = st.number_input("Monthly Income", 10000, 500000, 50000)
PitchSatisfactionScore = st.slider("Pitch Satisfaction Score", 1, 5, 3)
ProductPitched = st.selectbox("Product Pitched", ["Basic", "Standard", "Deluxe", "Super Deluxe", "King"])
NumberOfFollowups = st.number_input("Number of Followups", 0, 10, 2)
DurationOfPitch = st.number_input("Duration of Pitch", 5, 60, 20)

# Prediction
if st.button("Predict"):

    input_data = pd.DataFrame({
        "Age": [Age],
        "TypeofContact": [TypeofContact],
        "CityTier": [CityTier],
        "Occupation": [Occupation],
        "Gender": [Gender],
        "NumberOfPersonVisiting": [NumberOfPersonVisiting],
        "PreferredPropertyStar": [PreferredPropertyStar],
        "MaritalStatus": [MaritalStatus],
        "NumberOfTrips": [NumberOfTrips],
        "Passport": [Passport],
        "OwnCar": [OwnCar],
        "NumberOfChildrenVisiting": [NumberOfChildrenVisiting],
        "Designation": [Designation],
        "MonthlyIncome": [MonthlyIncome],
        "PitchSatisfactionScore": [PitchSatisfactionScore],
        "ProductPitched": [ProductPitched],
        "NumberOfFollowups": [NumberOfFollowups],
        "DurationOfPitch": [DurationOfPitch]
    })

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("Customer is likely to purchase the package")
    else:
        st.error("Customer is unlikely to purchase the package")