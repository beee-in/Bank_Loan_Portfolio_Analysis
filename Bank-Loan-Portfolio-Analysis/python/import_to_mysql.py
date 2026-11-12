"""Template for importing a cleaned loan dataset into MySQL.

Configure credentials through environment variables. Never commit secrets.
Review the dataset schema and create a matching table before running.
"""
import os
import pandas as pd
import mysql.connector

DATA_PATH = os.getenv("LOAN_CSV_PATH", "data/processed/clean_loan.csv")

required = ["loan_amnt", "term", "int_rate", "installment", "grade",
            "emp_length", "home_ownership", "annual_inc", "loan_status"]

df = pd.read_csv(DATA_PATH, usecols=required)
df["int_rate"] = (
    df["int_rate"].astype(str).str.replace("%", "", regex=False).astype(float)
)

connection = mysql.connector.connect(
    host=os.getenv("MYSQL_HOST", "localhost"),
    user=os.environ["MYSQL_USER"],
    password=os.environ["MYSQL_PASSWORD"],
    database=os.getenv("MYSQL_DATABASE", "bank_loan"),
)

try:
    cursor = connection.cursor()
    placeholders = ", ".join(["%s"] * len(required))
    columns = ", ".join(f"`{column}`" for column in required)
    query = f"INSERT INTO loan_data ({columns}) VALUES ({placeholders})"
    cursor.executemany(query, df[required].itertuples(index=False, name=None))
    connection.commit()
    cursor.close()
    print(f"Imported {len(df)} rows.")
finally:
    connection.close()
