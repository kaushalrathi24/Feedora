import mysql.connector as sql

mydb = sql.connect(
    host="localhost",
    user="root",
    passwd="oneminutenineseconds")

print(mydb)
