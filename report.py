import os
import mysql.connector
import pandas as pd


mydb = mysql.connector.connect(
    "user": "testuser",
    "password": "pass",
    "host": "10.4.5.16",
    "database": "test_schema",
)

sql = "SELECT * FROM persons;"
mycursor = mydb.cursor()
mycursor.execute(sql)
myresult = mycursor.fetchall()

df = pd.DataFrame()
for x in myresult:
    df2 = pd.DataFrame(list(x)).T
    df = pd.concat([df, df2])

df.to_csv('sql-data.csv')