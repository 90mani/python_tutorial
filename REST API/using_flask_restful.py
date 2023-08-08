# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import mysql.connector

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)
mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6635850",
    password="WWhxxlLRHb",
    database="sql6635850",
)
mycursor = mydb.cursor()


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello(Resource):
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    def get(self):
        mycursor.execute("SELECT * from user_details")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})

    # Corresponds to POST request
    def post(self):
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
            requestPayload["status"],
        )
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({"data": str(mycursor.rowcount) + "record inserted."}), 201


# another resource to calculate the square of a number
class Square(Resource):
    def get(self, num):
        return jsonify({"square": num**2})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, "/")
api.add_resource(Square, "/square/<int:num>")


# driver function
if __name__ == "__main__":
    app.run(debug=True)
