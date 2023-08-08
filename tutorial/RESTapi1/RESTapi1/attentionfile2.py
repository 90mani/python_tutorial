
from flask import Flask, jsonify, request
import mysql.connector
app = Flask(__name__)
mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6636952",
    password="9JJrXbm37m",
    database="sql6636952",
    )
mycursor = mydb.cursor()

@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "Server starting"
        return jsonify({"data": data})
@app.route("/student", methods=["GET", "POST"])
def getstudent():
    if request.method == "GET":
        mycursor.execute("SELECT * from stu_attendance")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})
    if request.method == "POST":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["Roll NO"])
        sql = "INSERT INTO stu_attendance (Roll No, Name,Degree,Course,Sem,attendance) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (requestPayload["Roll No"], requestPayload["Name"],requestPayload["Degree"],requestPayload["Course"],requestPayload["Sem"], requestPayload["attendance"])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201

#@app.route("/student", methods=["DELETE"])
#def deletestudent():
   # if request.method == "DELETE":
    #    sql = "DELETE FROM stu_attendance WHERE Name = %s"
     #   adr = ("Bhuvi", )

  #      mycursor.execute(sql, adr)

 #       mydb.commit()

#print(mycursor.rowcount, "record(s) deleted")




# @app.route("/student", methods=["POST"])
#	 def deletestudent():


if __name__ == "__main__":
    app.run(debug=True)