from flask import Flask, jsonify, request
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
    host="local host",
    user="girija",
    password="girima",
    database="mydatabase",
)
mycursor = mydb.cursor()


@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "server starting"
        return jsonify({"data": data})


@app.route("/employee", methods=["GET", "POST"])
def getstudent():
    if request.method == "GET":
        mycursor.execute("SELECT * from employee.details")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})
    

if __name__ == "__main__":
    app.run(debug=True)
