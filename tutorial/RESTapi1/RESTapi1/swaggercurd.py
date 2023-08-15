# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
import mysql.connector


# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

# swagger configuration
app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="student-mgnt",
            version="v1",
            plugins=[MarshmallowPlugin()],
            openapi_version="2.0.0",
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",  # URI to access API Doc JSON
        "APISPEC_SWAGGER_UI_URL": "/swagger-ui/",  # URI to access UI of API Doc
    }
)
docs = FlaskApiSpec(app)

# database connectivity
mydb = mysql.connector.connect(
  host="127.0.0.1",
  port="3307",
  user="root",
  password="admin",
  database="student-mgnt",
)
mycursor = mydb.cursor()

# Request schema for post api
class studentReuqetBody(Schema):
    id = fields.Int(required=True, description="student id")
    name = fields.String(required=True, description="student name")
    course = fields.String(required=True, description="student course")
    sem = fields.Int(required=True, description="student sem")
    attendance = fields.Int(required=True, description="student attendance")
    
# Request schema for delete api
class DeleteReuqetBody(Schema):
    id = fields.Int(required=True, description="student id")

# Request schema for put api
class UpdateReuqetBody(Schema):
    id = fields.Int(required=True, description="student id")
    name = fields.String(required=True, description="student name")

#welcome page    
class Hello(MethodResource, Resource):
    @doc(description="It's my first get hello api", tags=["HELLO API"])

    def get(self):
        return jsonify({"data": "server start"})

# crud operation
class student(MethodResource, Resource):
    @doc(description="Fet all student data", tags=["student"])
    def get(self, **kwargs):
        if request.method == "GET":
            mycursor.execute("SELECT * from student")
            myresult = mycursor.fetchall()
            return jsonify({"data": myresult})

    @doc(description="insert student data", tags=["student"])
    @use_kwargs(studentReuqetBody, location=("json"))
    def post(self, **kwargs):
        if request.method == "POST":
            requestPayload = request.get_json()
            id = requestPayload["id"]
            name = requestPayload["name"]
            course = requestPayload["course"]
            sem  = requestPayload["sem"]
            attendance = requestPayload["attendance"]
                               
            sql = "INSERT INTO student (id,name,course,sem,attendance) VALUES (%s,%s,%s,%s,%s)"
            val = (id,name,course,sem,attendance)
            mycursor.execute(sql, val)
            mydb.commit()
            return jsonify({"data": str(mycursor.rowcount) + "record inserted"})

    @doc(description="delete student data", tags=["student"])
    @use_kwargs(DeleteReuqetBody, location=("json"))
    def delete (self, **kwargs):
        if request.method == "DELETE":
            requestPayload = request.get_json()
            id = requestPayload["id"]
            sql = "DELETE FROM student WHERE id = " + str(requestPayload["id"])
            #val=(id) 
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount)
            return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"})

    @doc(description="UPDATE  student data", tags=["student"])
    @use_kwargs(UpdateReuqetBody, location=("json"))
    def put (self, **kwargs):
        if request.method == "PUT":
            requestPayload = request.get_json()
            id = requestPayload["id"]
            name = requestPayload["name"]
            sql =("UPDATE student SET name = '" + str(requestPayload["name"]) +"' WHERE id = " + str(requestPayload["id"]))
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            #print(mycursor.rowcount)
            return jsonify({'message': str(mycursor.rowcount) + "record(s) updated"})

api.add_resource(Hello, "/hello")
api.add_resource(student, "/student/")

docs.register(Hello)
docs.register(student)

# driver function
if __name__ == "__main__":
    app.run(debug=True)
