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
            title="Employee leave Management",
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
    user="root",
    password="saranya-123",
    database="leave_management",
)
mycursor = mydb.cursor()

# Request schema for post api
class EmployeeReuqetBody(Schema):
    Name = fields.String(required=True, description="employee Name")
    ID = fields.Int(required=True, description="employee ID")
    Email = fields.String(required=True, description="employee Email")
    Location = fields.String(required=True, description="employee Location")

# Request schema for delete api
class DeleteReuqetBody(Schema):
    ID = fields.Int(required=True, description="employee ID")

# Request schema for put api
class UpdateReuqetBody(Schema):
    Name = fields.String(required=True, description="employee Name")
    ID = fields.Int(required=True, description="employee ID")

#welcome page    
class Hello(MethodResource, Resource):
    @doc(description="It's my first get hello api", tags=["Hello API"])

    def get(self):
        return jsonify({"data": "hello world"})

# crud operation
class Employee(MethodResource, Resource):
    @doc(description="Fet all employees data", tags=["Employee"])
    def get(self, **kwargs):
        if request.method == "GET":
            mycursor.execute("SELECT * from employee_info")
            myresult = mycursor.fetchall()
            return jsonify({"data": myresult})

    @doc(description="insert employee data", tags=["Employee"])
    @use_kwargs(EmployeeReuqetBody, location=("json"))
    def post(self, **kwargs):
        if request.method == "POST":
            requestPayload = request.get_json()
            Name = requestPayload["Name"]
            ID = requestPayload["ID"]
            Email = requestPayload["Email"]
            Location = requestPayload["Location"]
            sql = "INSERT INTO employee_info (Name,ID,Email,Location) VALUES (%s,%s,%s,%s)"
            val = (Name, ID, Email,Location)
            mycursor.execute(sql, val)
            mydb.commit()
            return jsonify({"data": str(mycursor.rowcount) + "record inserted"})

    @doc(description="delete employee data", tags=["Employee"])
    @use_kwargs(DeleteReuqetBody, location=("json"))
    def delete (self, **kwargs):
        if request.method == "DELETE":
            requestPayload = request.get_json()
            ID = requestPayload["ID"]
            sql = "DELETE FROM employee_info WHERE ID = " + str(requestPayload["ID"])
            #val=(ID) 
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount)
            return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"})

    @doc(description="UPDATE  employee data", tags=["Employee"])
    @use_kwargs(UpdateReuqetBody, location=("json"))
    def put (self, **kwargs):
        if request.method == "PUT":
            requestPayload = request.get_json()
            Name = requestPayload["Name"]
            ID = requestPayload["ID"]
            sql =("UPDATE employee_info SET Name = '" + str(requestPayload["Name"]) +"' WHERE ID = " + str(requestPayload["ID"]))
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            #print(mycursor.rowcount)
            return jsonify({'message': str(mycursor.rowcount) + "record(s) updated"})
            



api.add_resource(Hello, "/hello")
api.add_resource(Employee, "/Employee/")

docs.register(Hello)
docs.register(Employee)

# driver function
if __name__ == "__main__":
    app.run(debug=True)
