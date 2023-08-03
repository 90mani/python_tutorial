# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request
import mysql.connector

# creating a Flask app
app = Flask(__name__)


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="saranya-123",
    database="leave_management",
)
mycursor = mydb.cursor()

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "Server started"
        return jsonify({"data": data})

@app.route("/employees", methods=["GET", "POST"])
def getEmployee():
    if request.method == "GET":
        mycursor.execute("SELECT * from employee_info")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})
    if request.method == "POST":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["Name"])
        sql = "INSERT INTO employee_info (Name, ID, Email, Location) VALUES (%s,%s,%s,%s)"
        val = (requestPayload["Name"], requestPayload["ID"],requestPayload["Email"],requestPayload["Location"])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201
    
@app.route("/employees", methods=["DELETE"])
def deleteEmployee():
    if request.method == "DELETE":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["ID"])
        sql = "DELETE FROM employee_info WHERE ID = " + str(requestPayload["ID"]) 
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"}), 200

@app.route("/employees", methods=["PUT"])
def updateEmployee():
    if request.method == "PUT":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["Name","ID"])
        sql =("UPDATE employee_info SET Name = '" + str(requestPayload["Name"]) +"' WHERE ID = " + str(requestPayload["ID"]))
        #val = (requestPayload["Name"],requestPayload["ID"])
        mycursor.execute(sql,)
        mydb.commit()
        print(mycursor.rowcount, "record(s) updated")
        return jsonify({"data": str(mycursor.rowcount) + "record(s) updated"}), 200
    


# driver function
if __name__ == "__main__":
    app.run(debug=True)





