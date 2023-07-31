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
        data = "server starting"
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
        sql = "INSERT INTO user_details (user_id, username) VALUES (%s, %s)"
        val = (requestPayload["userId"], requestPayload["name"])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201


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
