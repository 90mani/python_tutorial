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
        mycursor.execute("SELECT * from Attention")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})
    if request.method == "POST":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["Roll No"])
        sql = "INSERT INTO Attention (Roll No,Name,Degree,Course,Sem,Attention) VALUES (%s, %s)"
        val = (requestPayload["Roll NO"], requestPayload["name"], requestPayload["Degree"], (requestPayload["Course"], requestPayload["Sem"], requestPayload["Attention"])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201


# @app.route("/student", methods=["POST"])
# def insertStudent():
#     requestPayload = request.get_json()
#     print(requestPayload)
#     print(requestPayload["Roll No"])
      sql = "INSERT INTO Attention (Roll No,Name,Degree,Course,Sem,Attention) VALUES (%s, %s)"
      val = (requestPayload["Roll NO"], requestPayload["name"], requestPayload["Degree"], (requestPayload["Course"], requestPayload["Sem"], requestPayload["Attention"])

#     
#     mycursor.execute(sql, val)
#     mydb.commit()
#     return jsonify({"data": str(mycursor.rowcount) + "record inserted."})


if __name__ == "__main__":
    app.run(debug=True)