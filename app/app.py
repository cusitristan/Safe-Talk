import mysql.connector
import time
try:
  mydb = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="courses"
  )
except:
  print("Could not connect to MySQL, sleeping 30 sec then trying again")
  time.sleep(30)
  try:
    mydb = mysql.connector.connect(
      host="mysql",
      user="root",
      password="root",
      database="mydb"
    )
  except:
    print("Could not connect to MySQL after 30sec")
    
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users;")

for row in mycursor:
    print(row)

while 1:
  print("looping")
  time.sleep(5)