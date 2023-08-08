# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import mysql.connector

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="3307",
  user="root",
  password="admin",
  database="student-mgnt",
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

        return jsonify({'message': 'hello world'})

    def get(self):
        mycursor.execute("SELECT * from student")
        myresult = mycursor.fetchall()
        return jsonify({"data": myresult})

    # Corresponds to POST request
    def post(self):
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["id"])
        sql = "INSERT INTO student (id, name, course, sem, attendance) VALUES (%s,%s,%s,%s,%s)"
        val = (requestPayload["id"], requestPayload["name"], requestPayload["course"], requestPayload["sem"],requestPayload["attendance"])
        mycursor.execute(sql, val)
        mydb.commit()
        return jsonify({'message':str(mycursor.rowcount ) + "record inserted."}),201


    #def delete(self):
     #   requestPayload = request.get_json()
      #  print(requestPayload)
       # print(requestPayload["name"])
        #sql = "DELETE FROM srudent WHERE name = " + str(requestPayload["name"]) 
        #print(sql)
        #mycursor.execute(sql)
        #mydb.commit()
        #print(mycursor.rowcount, "record(s) deleted")
        #return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"}), 200  

# another resource to calculate the square of a number
class Square(Resource):

    def get(self, num):

        return jsonify({'square': num**2})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/')
api.add_resource(Square, '/square/<int:num>')


# driver function
if __name__ == '__main__':

    app.run(debug = True)
