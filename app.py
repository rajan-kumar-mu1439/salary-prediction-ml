import streamlit as st
import joblib 
import numpy as np


model = joblib.load("Linear_model.pkl")

st.title("Salary Prediction:")

st.write("You can get estimations for the salaries of the company employee.")

years = st.number_input("Enter the years at company.",value=1, step=1, min_value=0)
jobrate = st.number_input("Enter the Job Rate",value=3.5, step=0.5, min_value=0.0)

x = [years, jobrate]

predict = st.button("Press the button for salaey prediction")
if predict:

    x1 = np.array([x])
    prediction = model.predict(x1)[0]
    st.write(f"Salary Prediction is :- {prediction:,.2f}")

else:
    print("")

