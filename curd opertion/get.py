from flask import Flask, jsonify, request
import mysql.connector


app = Flask(__name__)


mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="2810",
    database="studend",
)
mycursor = mydb.cursor()


@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "server started"
        return jsonify({"data":data})
    
@app.route("/student", methods=["GET","POST"])   
def getstudent():
    if request.method == "GET":
        mycursor.execute("SELECT * from marksheet")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})
    if request.method == "POST":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["id"])
        sql = "INSERT INTO marksheet (id, name, mark, grade) VALUES (%s, %s, %s,%s)"
        val = (requestPayload["id"], requestPayload["name"], requestPayload["mark"], requestPayload["grade"])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201 
        
        
@app.route("/student", methods=["DELETE"])    
def deletestudent():
    if request.method == "DELETE":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["id"])  
        sql = "DELETE FROM marksheet WHERE id = " + str(requestPayload["id"])
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) deleted")
        return jsonify({"data": str(mycursor.rowcount) +"record(s) deleted"}),200

@app.route("/student", methods=["PUT"]) 
def updatestudent():
    if request.method == "PUT":
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["name"])  
        sql = "UPDATE marksheet SET name = '" + str(requestPayload["name"]) +"' WHERE ID =" + str(requestPayload["id"])
        print(sql)
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) updated")
        return jsonify({"data": str(mycursor.rowcount) +"record(s) updated"}),200    
 


if __name__ == "__main__":
    app.run(debug=True)
    
     
     
   


     



    






