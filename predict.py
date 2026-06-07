import joblib
import numpy as np


# Load trained model
model = joblib.load("churn_model.pkl")


def predict_churn(customer_data):

    prediction = model.predict([customer_data])

    return prediction[0]


# Example customer data
sample_customer = [
    1,      # gender
    0,      # SeniorCitizen
    1,      # Partner
    0,      # Dependents
    5,      # tenure
    1,      # PhoneService
    0,      # MultipleLines
    1,      # InternetService
    1,      # OnlineSecurity
    0,      # OnlineBackup
    1,      # DeviceProtection
    0,      # TechSupport
    1,      # StreamingTV
    1,      # StreamingMovies
    0,      # Contract
    1,      # PaperlessBilling
    2,      # PaymentMethod
    50.5,   # MonthlyCharges
    300.2   # TotalCharges
]


result = predict_churn(sample_customer)


if result == 1:
    print("Customer likely to churn")
else:
    print("Customer likely to stay")