#using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
import mysql.connector

#creating the flask app
app =Flask(__name__)

#creating an API object
api=Api(app)

mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="3307",
  user="root",
  password="admin",
  database="student-mgnt",
) 
mycrusor = mydb.cursor()
#making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.
class Hello (Resource):

    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource

    def get(self):
        return jsonify({'message': 'server starting'})
    
    def get(self):
        mycrusor.execute("SELECT * from student")
        myresult = mycrusor.fetchall()
        return jsonify({'data': myresult})
        # corresponds to the POST request
    def post(self):
        requestPayload =request.get_json()
        print(requestPayload)
        print(requestPayload["id"])
        sql ="INSERT INTO student(id, name, course, sem, attendance)VALUES(%s,%s,%s,%s,%s)"
        val =(requestPayload["id"], requestPayload["name"], requestPayload["course"], requestPayload["sem"], requestPayload["attendance"])
        mycrusor.execute(sql,val)
        mydb.commit()
        return jsonify({'data' : str(mycrusor.rowcount)+"record inserted"})
    def delete(self):
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload["id"])
        sql = "DELETE FROM student WHERE id = " + str(requestPayload["id"]) 
        print(sql)
        mycrusor.execute(sql)
        mydb.commit()
        print(mycrusor.rowcount)
        return jsonify({'data': str(mycrusor.rowcount) + "record(s) deleted"})
    def updatestudent():
        requestPayload = request.get_json()
        print(requestPayload)
        print(requestPayload ["id"])
        sql =("UPDATE student SET id = '" + str(requestPayload["id"]) +"' WHERE name = " + str(requestPayload["name"]))
        print(sql)
        #val = (requestPayload["name"],requestPayload["id"])
        mycursor.execute(sql)
        mydb.commit()
        print(mycursor.rowcount, "record(s) updated")
        return jsonify({"data": str(mycursor.rowcount) + "record(s) updated"})
    
    # another resource to calculate the square of a number
class Square(Resource):
    def get(self,num):
        return jsonify({'square':num**2})
    # adding the defined resources along with their corresponding urls
api.add_resource(Hello, '/student')
api.add_resource(Square, '/square/<int:num>')


# driver function
if __name__ == '__main__':

    app.run(debug = True)