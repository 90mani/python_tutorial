#sql stored procedure

import mysql.connector

mydb =mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="2003@saran",
    database="employee_mgnt",
)
obj = mydb.cursor()
obj.callproc("employee_details")
for result in obj.stored_results():
    details = result.fetchall()

for det in details:
    print(det)

obj.close()
mydb.close()