from flask import Flask, jsonify, request
import mysql.connector

# creating a Flask app
app = Flask(__name__)


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="admin",
    port="3307",
    database="student-mgnt",

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


@app.route("/student", methods=["GET", "POST"])
def getstudent():
    if request.method == "GET":
        mycursor.execute("SELECT * from student")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})
    if request.method == "POST":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["id"])
        sql = "INSERT INTO student(id, name, course, sem, attendance) VALUES (%s,%s,%s,%s,%s)"
        val = (requestPayload["id"], requestPayload["name"], requestPayload["course"], requestPayload["sem"], requestPayload["attendance"])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201

@app.route("/student", methods=["DELETE"])
def deletestudent():
   if request.method == "DELETE":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["id"])
        sql = "DELETE FROM student WHERE id = " + str(requestPayload["id"]) 
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"}), 200

@app.route("/student", methods=["PUT"])
def updatestudent():
    if request.method == "PUT":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload ["name"])
        sql =("UPDATE student SET name = '" + str(requestPayload["name"]) +"' WHERE id = " + str(requestPayload["id"]))
        print(sql)
        #val = (requestPayload["id"],requestPayload["name"])
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) updated")
        return jsonify({"data": str(mycursor.rowcount) + "record(s) updated"}), 200



# driver function
if __name__ == "__main__":
    app.run(debug=True)




