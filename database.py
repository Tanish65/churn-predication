import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="tanishmysql123",
    database="churn_db"
)

cursor = conn.cursor()

print("Database Connected")