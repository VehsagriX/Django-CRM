import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='vehsagri',
    passwd='respect2002',
    )

# prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database
cursorObject.execute("CREATE DATABASE djangodb")
print("All Done!")

