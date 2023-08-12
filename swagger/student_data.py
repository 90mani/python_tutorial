from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs
import mysql.connector


app = Flask(__name__)

api = Api(app)


app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="Student Management",
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
    host="sql6.freesqldatabase.com",
    user="sql6637633",
    password="JlHqEM7Xl5",
    database="sql6637633",
)
mycursor = mydb.cursor()


class StudentReuqetBody(Schema):
    userId = fields.Int(required=True, description="Student id")
    u_name = fields.String(required=True, description="Student name")
    passcode = fields.String(required=True, description="Student name")
    number = fields.Int(required=True, description="Student name")
    no_experiance = fields.Int(required=False, description="Student name")


class Hello(MethodResource, Resource):
    @doc(description="It's my first get hello api", tags=["Hello API"])
    def get(self):
        return jsonify({"data": "hello world"})


class student(MethodResource, Resource):
    @doc(description="get student data", tags=["Student"])
    def get(self):
        if request.method == "GET":
            mycursor.execute("SELECT * from employee")
            myresult = mycursor.fetchall()
            return jsonify({"data": myresult})

    @doc(description="insert student data", tags=["Student"])
    @use_kwargs(StudentReuqetBody, location=("json"))
    def post(self, **kwargs):
        if request.method == "POST":
            requestPayload = request.get_json()
            userId = requestPayload["userId"]
            name = requestPayload["u_name"]
            passcode = requestPayload["passcode"]
            number = requestPayload["number"]
            no_experiance = requestPayload["no_experiance"]
            sql = "INSERT INTO employee (employee_id,name,password,phone_number,experiance) VALUES (%s,%s,%s,%s,%s)"
            val = (userId, name, passcode, number, no_experiance)
            mycursor.execute(sql, val)
            mydb.commit()
            return jsonify({"data": str(mycursor.rowcount) + "record inserted"})


api.add_resource(Hello, "/hello")
api.add_resource(student, "/student")


docs.register(Hello)
docs.register(student)

if __name__ == "__main__":
    app.run(debug=True)
