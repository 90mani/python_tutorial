from flask import Flask, jsonify, request
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="girija",
    password="girima",
    database="author",
)
mycursor = mydb.cursor()


@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "Server starting"
        return jsonify({"data": data})
    
#POST METHOD


@app.route("/author", methods=["GET", "POST"])
def getauthor():
    if request.method == "GET":
        mycursor.execute("SELECT * from author.details")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})
    if request.method == "POST":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["auid"])
        sql = "INSERT INTO author.details (auid, name, title, price, year, country) VALUES (%s,%s,%s,%s,%s,%s)"
        val = (
            requestPayload["auid"],
            requestPayload["name"],
            requestPayload["title"],
            requestPayload["price"],
            requestPayload["year"],
            requestPayload["country"],
    
        )
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201


@app.route("/author", methods=["DELETE"])
def deleteauthor():
    if request.method == "DELETE":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["auid"])
        sql = "DELETE FROM author.details WHERE auid = " + str(
            requestPayload["auid"]
        )
        print(sql)

        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"}), 200
    
#DELETE METHOD


# @app.route("/author", methods=["POST"])
# def deletetauthor():
#     requestPayload = request.get_json()
#     print(requestPayload)
#     print(requestPayload["auid"])
#     sql = "INSERT INTO author.details (auid,name) VALUES (%s, %s)"
#     val = (requestPayload["auid"], requestPayload["name"])
#     mycursor.execute(sql, val)
#     mydb.commit()
#     return jsonify({"data": str(mycursor.rowcount) + "record inserted."})


if __name__ == "__main__":
    app.run(debug=True)
