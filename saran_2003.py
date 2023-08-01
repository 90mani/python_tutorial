from flask import Flask, jsonify, request
import mysql.connector


app = Flask(__name__)


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
        val = (requestPayload["userId"], requestPayload["u_name"],requestPayload["f_name"],requestPayload["lastname"],requestPayload["gender"],
                requestPayload["password"],requestPayload["status"])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201

@app.route("/student", methods=["DELETE"])
def deletestudent():
    if request.method == "DELETE":
        sql = "DELETE FROM user_details WHERE u_name = %s"
        adr = ("kani21", )

        mycursor.execute(sql, adr)

        mydb.commit()

        print(mycursor.rowcount, "record(s) deleted")
    



# @app.route("/student", methods=["POST"])
# def insertStudent():
#     requestPayload = request.get_json()
#     print(requestPayload)
#     print(requestPayload["userId"])
#     sql = "INSERT INTO user_details (user_id, username) VALUES (%s, %s)"
#     val = (requestPayload["userId"], requestPayload["name"])
#     mycursor.execute(sql, val)
#     mydb.commit()
#     return jsonify({"data": str(mycursor.rowcount) + "record inserted."})


if __name__ == "__main__":
    app.run(debug=True)