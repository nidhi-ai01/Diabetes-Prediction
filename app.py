import streamlit as st
import pandas as pd
import joblib

# Load the trained model
model = joblib.load('diabetes_model.joblib')

# App Title
st.title('Diabetes Prediction App')

st.write("Enter the patient's details below to predict the likelihood of diabetes.")

# Create input fields for user
# Use columns for a better layout
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.number_input('Pregnancies', min_value=0, max_value=20, value=1)
    bp = st.number_input('Blood Pressure (mm Hg)', min_value=0, max_value=122, value=69)
    insulin = st.number_input('Insulin (mu U/ml)', min_value=0, max_value=846, value=79)
    dpf = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.47, format="%.2f")

with col2:
    glucose = st.number_input('Glucose (mg/dL)', min_value=0, max_value=200, value=120)
    skin_thickness = st.number_input('Skin Thickness (mm)', min_value=0, max_value=99, value=20)
    bmi = st.number_input('BMI (kg/m²)', min_value=0.0, max_value=68.0, value=31.4, format="%.1f")
    age = st.number_input('Age (years)', min_value=21, max_value=81, value=33)

# Predict button
if st.button('Predict'):
    # Create a dataframe from the inputs
    input_data = pd.DataFrame([[pregnancies, glucose, bp, skin_thickness, insulin, bmi, dpf, age]],
                              columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])

    # Make prediction
    prediction = model.predict(input_data)
    prediction_proba = model.predict_proba(input_data)

    # Display the result
    st.subheader('Prediction Result')
    if prediction[0] == 1:
        st.error(f'The patient is likely to have diabetes. (Confidence: {prediction_proba[0][1]*100:.2f}%)')
    else:
        st.success(f'The patient is not likely to have diabetes. (Confidence: {prediction_proba[0][0]*100:.2f}%)')