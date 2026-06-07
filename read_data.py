import pandas as pd 
df=pd.read_csv(r"C:\Users\Lenovo\OneDrive\Desktop\customer churn predication\WA_Fn-UseC_-Telco-Customer-Churn.csv")
# print(df.head())
# print(df.shape)
# print(df.columns)
# print(df.isnull().sum())
# df.drop("customerID", axis=1, inplace=True)

# print(df.head())
# from sklearn.preprocessing import LabelEncoder

# le = LabelEncoder()

# for column in df.columns:
#     if df[column].dtype == 'object':
#         df[column] = le.fit_transform(df[column])

# print(df.head())
X = df.drop("Churn", axis=1)

y = df["Churn"]

print(X.head())
print(y.head())