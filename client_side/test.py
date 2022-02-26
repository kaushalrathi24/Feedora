import random
import hashlib
import string
import mysql.connector as sql


mydb = sql.connect(
    host='localhost',
    user='root',
    passwd='oneminutenineseconds',
    database='news')

cursor = mydb.cursor()

cursor.execute("select link from articles")
result = cursor.fetchall()
print(type(result))
print(result)
