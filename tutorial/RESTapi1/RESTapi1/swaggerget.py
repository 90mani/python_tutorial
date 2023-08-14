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

#creating the flask app
app =Flask(__name__)

#creating an API object
api=Api(app)

app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="student_attendance",
            version="v1",
            plugins=[MarshmallowPlugin()],
            openapi_version="2.0.0",
        ),
        "APISPEC_SWAGGER_URL": "/swagger/",  # URI to access API Doc JSON
        "APISPEC_SWAGGER_UI_URL": "/swagger-ui/",  # URI to access UI of API Doc
    }
)
docs = FlaskApiSpec(app)


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

class StudentReuqetBody(Schema):
    id = fields.Int(required=True, description="Student id")
    name = fields.String(required=True, description="Student name")
    course = fields.String(required=True, description="Student name")
    sem = fields.Int(required=True, description="Student name")
    attendance = fields.Int(required=False, description="Student name")


class Hello(MethodResource, Resource):
    @doc(description="It's my first get hello api", tags=["Hello API"])
    def get(self):
        return jsonify({"data": "hello world"})
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resouce
    
class student(MethodResource,Resource):

    @doc(description = "get student datd", tags = ["student"])

    def get(student):
        mycrusor.execute("SELECT * from student")
        myresult = mycrusor.fetchall()
        return jsonify({'data': myresult})
#Corresponds to POST request

    @doc(description="insert student data", tags=["Student"])
    @use_kwargs(StudentReuqetBody, location=("json"))
    def post(self, **kwargs):
        if request.method == "POST":
            requestPayload = request.get_json()
            id = requestPayload["id"]
            name = requestPayload["name"]
            course = requestPayload["course"]
            sem = requestPayload["sem"]
            attendance = requestPayload["attendance"]
            sql = "INSERT INTO student (id,name,course,sem,attendance) VALUES (%s,%s,%s,%s,%s)"
            val = (id,name,course,sem,attendance)
            mycrusor.execute(sql, val)
            mydb.commit()
            return jsonify({"data": str(mycrusor.rowcount) + "record inserted"})
   

api.add_resource(Hello,"/hello")  
api.add_resource(student,"/student")  
        

docs.register(Hello)
docs.register(student)

# driver function
if __name__ == '__main__':

    app.run(debug = True)


