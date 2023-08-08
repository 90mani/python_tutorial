import mysql.connector

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="saranya-123",
    database="leave_management",
)


class EmployeeService:
    mycursor = mydb.cursor()


def geEmployeeInfo(self):
    mycursor.execute("SELECT * from employee_info")
    myresult = mycursor.fetchall()
    return myresult


def addEmployeeIno(self, requestJosn):
    print(requestJosn)
    print(requestJosn["Name"])
    sql = "INSERT INTO employee_info (Name, ID, Email, Location) VALUES (%s,%s,%s,%s)"
    val = (
        requestJosn["Name"],
        requestJosn["ID"],
        requestJosn["Email"],
        requestJosn["Location"],
    )
    mycursor.execute(sql, val)
    mydb.commit()
    return mycursor.rorowcount
