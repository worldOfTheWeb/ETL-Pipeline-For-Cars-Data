import pandas as pd
from datetime import date

import mysql.connector as msql
from mysql.connector import Error


carsData = pd.read_csv('/home/tarang/Tarang/Python/Project_1/cars.csv', sep= ';')
# df.insert(9, column="Load_Date", value="")
carsData['Load_Date'] = pd.to_datetime('today').strftime("%d-%m-%Y")
df = carsData
df.head()
# print(df.head())

try:
    conn = msql.connect(host='localhost', user='root', password='root')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE carsdb")
        print("cars database is created")
except Error as e:
    print("Error", e)


try:
    conn = msql.connect(host='localhost', database='carsdb', user='root', password='root')
    if conn.is_connected():
        cursor = conn.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)
        cursor.execute('DROP TABLE IF EXISTS cars;')
        print('Creating table....')
# in the below line please pass the create table statement which you want #to create
        cursor.execute("CREATE TABLE cars(Car varchar(255),MPG varchar(255),Cylinders varchar(255),Displacement varchar(255),Horsepower varchar(255),Weight varchar(255),Acceleration varchar(255),Model varchar(255),Origin varchar(255),Load_Date varchar(255))")
        print("Table is created....")
        for i,row in carsData.iterrows():
            sql = "INSERT INTO carsdb.cars VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
            cursor.execute(sql, tuple(row))
            print("Record inserted")
            conn.commit()
except Error as e:
            print("Error while connecting to MySQL", e)


