import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


# Load dataset
df = pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\customer churn predication\WA_Fn-UseC_-Telco-Customer-Churn.csv")


# Remove customerID
df.drop("customerID", axis=1, inplace=True)


# Convert text into numbers
le = LabelEncoder()

for column in df.columns:
    if df[column].dtype == 'object':
        df[column] = le.fit_transform(df[column])


# Features and Target
X = df.drop("Churn", axis=1)
y = df["Churn"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create model
model = RandomForestClassifier()


# Train model
model.fit(X_train, y_train)


# Prediction
predictions = model.predict(X_test)


# Accuracy
accuracy = accuracy_score(y_test, predictions)

print("Model Accuracy:", accuracy)


# Save model
joblib.dump(model, "churn_model.pkl")

print("Model Saved Successfully")