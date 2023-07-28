import mysql.connector

mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6635849",
    password="AyPYNItaJp",
    database="sql6635849",
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * from employee")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
