import mysql.connector
import time

mydb = mysql.connector.connect(
  host="mysql",
  user="root",
  password="root",
  database="courses"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM teachers;")

for row in mycursor:
    print(row)

while 1:
	print("looping")
	time.sleep(5)