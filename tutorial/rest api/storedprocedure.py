import mysql.connector as myconn


mydb = myconn.connect(
    host="127.0.0.1",
    user="root",
    password="saranya-123",
    database="leave_management",
)
#mycursor = mydb.cursor()

obj = mydb.cursor()
obj.callproc("employee_details")

for result in obj.stored_results():
    details = result.fetchall()

for det in details:
    print(det)

obj.close()
mydb.close()

   
            



