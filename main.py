import streamlit as st
from predictor_help import predict

st.title('Health Insurance Predictor')

#--- Categorical options ---
categorical_options = {
    "gender": ["Male", "Female"],
    "region": ["Northwest", "Southeast", "Northeast", "Southwest"],
    "marital_status": ["Unmarried", "Married"],
    "bmi_category": ["Normal", "Obesity", "Overweight", "Underweight"],
    "smoking_status": [
        "No Smoking",
        "Regular",
        "Occasional",
    ],
    "employment_status": ["Salaried", "Self-Employed", "Freelancer"],
    "medical_history": [
        "Diabetes",
        "High blood pressure",
        "No Disease",
        "Diabetes & High blood pressure",
        "Thyroid",
        "Heart disease",
        "High blood pressure & Heart disease",
        "Diabetes & Thyroid",
        "Diabetes & Heart disease",
    ],
    "insurance_plan": ["Bronze", "Silver", "Gold"],
}

# Create four rows of three column each
row1 = st.columns(3)
row2 = st.columns(3)
row3 = st.columns(3)
row4 = st.columns(3)

# Assign inputs to grid
with row1[0]:
    age = st.number_input("Age", min_value=18, max_value=300, step=1)
with row1[1]:
    number_of_dependants = st.number_input("Number of dependants", min_value=0, max_value=20,  step=1)
with row1[2]:
    income_lakhs = st.number_input("Income Lakhs", min_value=0, max_value=200, step=1)

with row2[0]:
    genetical_risk = st.number_input("Genetical Risk", min_value=0, max_value=5, step=1)
with row2[1]:
    insurance_plan = st.selectbox("Insurance Plan", categorical_options["insurance_plan"])
with row2[2]:
    employment_status = st.selectbox("employment_status", categorical_options["employment_status"])

with row3[0]:
    gender = st.selectbox("Gender", categorical_options["gender"])
with row3[1]:
    martial_status = st.selectbox("Marital Status", categorical_options["marital_status"])
with row3[2]:
    bmi_category = st.selectbox("BMI Category", categorical_options["bmi_category"])

with row4[0]:
    smoking_status = st.selectbox("Smoking Status", categorical_options["smoking_status"])
with row4[1]:
    region = st.selectbox("Region", categorical_options["region"])
with row4[2]:
    medical_history = st.selectbox("Medical History", categorical_options["medical_history"])

# Create dictionary for input values
input_dict = {
    "Age": age,
    "Number of Dependants": number_of_dependants,
    "Income in Lakhs": income_lakhs,
    "Genetical Risk": genetical_risk,
    "Insurance Plan": insurance_plan,
    "Employment Status": employment_status,
    "Gender": gender,
    "Martial Status": martial_status,
    "BMI Category": bmi_category,
    "Smoking Status": smoking_status,
    "Region": region,
    "Medical History": medical_history
}

# Button to make prediction
if st.button("Predict"):
    prediction = predict(input_dict)
    st.success(f"Predicted Premiums : {prediction}")