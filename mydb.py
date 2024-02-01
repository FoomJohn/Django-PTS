import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",

)

cursorObject = dataBase.cursor()

#create database

cursorObject.execute("CREATE DATABASE foomdb")

print("all done!")