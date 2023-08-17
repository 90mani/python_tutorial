import mysql.connector as mycann
mydb = mycann.connect(
    host="127.0.0.1",
    user="root",
    password="2810",
    database="studend"
)
obj = mydb.cursor()
obj.callproc("student_information")

for result in obj.stored_results():
    details = result.fetchall()

for det in details:
    print(det)

obj.close()
mydb.close()