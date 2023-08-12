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
    u_name = fields.String(required=False, description="Student name")
    passcode = fields.String(required=False, description="Student name")
    number = fields.Int(required=False, description="Student name")
    no_experiance = fields.Int(required=False, description="Student name")


class student(MethodResource, Resource):
    @doc(description="Fet all employees data", tags=["Employee"])
    def get(self, **kwargs):
        if request.method == "GET":
            mycursor.execute("SELECT * from employee")
            myresult = mycursor.fetchall()
            return jsonify({"data": myresult})

    @doc(description="insert employee data", tags=["Employee"])
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


class SearchStudent(MethodResource, Resource):
    @doc(description="Get employee by id", tags=["Employee"])
    def get(self, id):
        if request.method == "GET":
            mycursor.execute("SELECT * from employee where employee_id = " + str(id))
            myresult = mycursor.fetchall()
            return jsonify({"data": myresult})


api.add_resource(student, "/employee")
api.add_resource(SearchStudent, "/employee/<int:id>")

docs.register(student)
docs.register(SearchStudent)

if __name__ == "__main__":
    app.run(debug=True)
