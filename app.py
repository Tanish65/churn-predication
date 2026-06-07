import streamlit as st
import joblib
from database import conn, cursor

# Load model
model = joblib.load("churn_model.pkl")

st.title("Customer Churn Prediction")

# Customer Information
gender = st.selectbox("Select Gender", ["Male", "Female"])

partner = st.selectbox("Has Partner?", ["Yes", "No"])

tenure = st.slider(
    "Customer Tenure (Months)",
    0,
    72
)

monthly_charges = st.number_input(
    "Monthly Charges",
    min_value=0.0
)

total_charges = st.number_input(
    "Total Charges",
    min_value=0.0
)

# Convert
gender = 1 if gender == "Male" else 0
partner = 1 if partner == "Yes" else 0


if st.button("Predict"):

    customer_data = [
        gender,
        0,
        partner,
        0,
        tenure,
        1,
        0,
        1,
        1,
        0,
        1,
        0,
        1,
        1,
        0,
        1,
        2,
        monthly_charges,
        total_charges
    ]

    prediction = model.predict([customer_data])

    if prediction[0] == 1:
        result = "Churn"
        st.error("⚠️ Customer likely to churn")

    else:
        result = "Stay"
        st.success("✅ Customer likely to stay")

    # Save prediction in MySQL
    query = """
    INSERT INTO predictions(
        customer_name,
        tenure,
        monthly_charges,
        total_charges,
        prediction
    )
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (
        "Customer",
        tenure,
        monthly_charges,
        total_charges,
        result
    )

    cursor.execute(query, values)

    conn.commit()