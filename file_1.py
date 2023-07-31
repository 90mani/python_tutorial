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


@app.route("/student", methods=["GET"])
def getstudent():
    mycursor.execute("SELECT * from user_details")
    myresult = mycursor.fetchall()
    return jsonify({"data": myresult})


if __name__ == "__main__":
    app.run(debug=True)
