#["GET","POST","PUT","DELETE" SQL and python connectivity query]

from flask import Flask,jsonify,request
import mysql.connector
app = Flask(__name__)

#Particular specify data base

mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6636952",
    password="9JJrXbm37m",
    database="sql6636952",
	def home():
    data = "Server starting"
    return jsonify({"data": data})

#To "GATHER" and "POST" more details in given table
@app.route("/student", methods=["GET", "POST"])

    def getstudent():

        print(requestPayload["Roll No"])

        sql = "INSERT INTO stu_attendance (Roll No, Name,Degree,Course,Sem,attendance) VALUES (%s,%s,%s,%s,%s,%s)"

        val = (

               requestPayload["Roll No"],

               requestPayload["Name"],

               requestPayload["Degree"],

               requestPayload["Course"],

               requestPayload["Sem"],

               requestPayload["attendance"]

               

               )

        mycursor.execute(sql, val)

        mydb.commit()

        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201




#To "UPDATE" or ADD details in given table






@app.route("/student", methods=["PUT"])

def updatestudent():

    if request.method == "PUT":

        requestPayload = request.get_json()

        print(requestPayload)

        print(requestPayload["Roll No"])

        sql ="UPDATE Name SET Name = Bhuvi WHERE Name= "+ str(

            requestPayload["Name"]

        )
        print(sql)
        mycursor.execute(sql)

        print(mycursor.rowcount, "record(s) updated")
        return jsonify({"data": str(mycursor.rowcount) + "record(s) updated"}),200
#To "DELETE" particular or more details in given table
@app.route("/student", methods=["DELETE"])
    def deletestudent():
    if request.method == "DELETE":

	def deletestudent():

        print(mycursor.rowcount, "record(s) deleted")

        return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"}), 200

    if __name__ == "__main__":
    app.run(debug=True)