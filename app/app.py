import mysql.connector
import time
#try connect, if it doesnt work wait 30 sec and try again 
#(this gives db container to boot up)
try:
  mydb = mysql.connector.connect(
    host="mysql",
    user="root",
    password="root",
    database="safedb"
  )
except:
  print("Could not connect to MySQL, sleeping 30 sec then trying again")
  time.sleep(30)
  try:
    mydb = mysql.connector.connect(
      host="mysql",
      user="root",
      password="root",
      database="safedb"
    )
  except:
    print("Could not connect to MySQL after 30sec")
    exit()
#create cursor which is used to query and itterate results
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM users;")

for row in mycursor:
    print(row)

while 1:
  print("looping")
  time.sleep(5)