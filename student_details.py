#["GET","POST","PUT","DELETE" SQL and python connectivity query]

from flask import Flask,jsonify,request
import mysql.connector


app = Flask(__name__)

#Particular specify data base


mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6635850",
    password="WWhxxlLRHb",
    database="sql6635850",
)
mycursor = mydb.cursor()


@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "Server starting"
        return jsonify({"data": data})

#To "GATHER" and "POST" more details in given table

@app.route("/student", methods=["GET", "POST"])
def getstudent():
    if request.method == "GET":
        mycursor.execute("SELECT * from user_details")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})
    if request.method == "POST":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["userId"])
        sql = "INSERT INTO user_details (user_id, username,first_name,last_name,gender,password,status) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (
               requestPayload["userId"],
               requestPayload["u_name"],
               requestPayload["f_name"],
               requestPayload["lastname"],
               requestPayload["gender"],
               requestPayload["password"],
               requestPayload["status"]
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
        print(requestPayload["u_name"])
        sql ="UPDATE username SET username = prabha WHERE username= "+ str(
            requestPayload["u_name"]
        )
        print(sql)
        mycursor.execute(sql)

        print(mycursor.rowcount, "record(s) updated")
        return jsonify({"data": str(mycursor.rowcount) + "record(s) updated"}),200

#To "DELETE" particular or more details in given table
    
@app.route("/student", methods=["DELETE"])
def deletestudent():
    if request.method == "DELETE":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["userId"])
        sql = "DELETE FROM user_details WHERE user_id = " + str(
            requestPayload["userId"]
        )
        print(sql)

        mycursor.execute(sql)

        print(mycursor.rowcount, "record(s) deleted")
        return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"}), 200

    

   

if __name__ == "__main__":
    app.run(debug=True)