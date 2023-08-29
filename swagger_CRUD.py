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
            title="Employee Management",
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
    user="girija",
    password="girima",
    database="employee",
)
mycursor = mydb.cursor()

# Request schema for post api
class employeeReuqetBody(Schema):
    id = fields.Int(required=True, description="employee id")
    name = fields.String(required=True, description="employee name")
    age = fields.Int(required=True, description="employee age")
    address = fields.String(required=True, description="employee address")

# Request schema for delete api
class DeleteReuqetBody(Schema):
    id = fields.Int(required=True, description="employee id")

# Request schema for put api
class UpdateReuqetBody(Schema):
    id = fields.Int(required=True, description="employee id")
    name = fields.String(required=True, description="employee name")

#welcome page    
class Hello(MethodResource, Resource):
    @doc(description="It's my first get hello api", tags=["Hello API"])

    def get(self):
        return jsonify({"data": "hello world"})

# crud operation
class employee(MethodResource, Resource):
    @doc(description="Fet all employee data", tags=["employee"])
    def get(self, **kwargs):
        if request.method == "GET":
            mycursor.execute("SELECT * from employee.profile")
            myresult = mycursor.fetchall()
            return jsonify({"data": myresult})
        
    @doc(description="insert employee data", tags=["employee"])
    @use_kwargs(employeeReuqetBody, location=("json"))
    def post(self, **kwargs):
        if request.method == "POST":
            requestPayload = request.get_json()
            id = requestPayload["id"]
            name = requestPayload["name"]
            age = requestPayload["age"]
            address = requestPayload["address"]
            sql = "INSERT INTO employee.profile (id,name,age,address) VALUES (%s,%s,%s,%s)"
            val = (id, name, age, address)
            mycursor.execute(sql, val)
            mydb.commit()
            return jsonify({"data": str(mycursor.rowcount) + "record inserted"}) 

    

    @doc(description="delete employee data", tags=["employee"])
    @use_kwargs(DeleteReuqetBody, location=("json"))
    def delete (self, **kwargs):
        if request.method == "DELETE":
            requestPayload = request.get_json()
            id = requestPayload["id"]
            sql = "DELETE FROM employee.profile WHERE id = " + str(requestPayload["id"])
            #val=(id) 
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount)
            return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"})

    @doc(description="UPDATE  employee data", tags=["employee"])
    @use_kwargs(UpdateReuqetBody, location=("json"))
    def put (self, **kwargs):
        if request.method == "PUT":
            requestPayload = request.get_json()
            id = requestPayload["id"]
            name = requestPayload["name"]
            sql =("UPDATE employee.profile SET name= '" + str(requestPayload["name"]) +"' WHERE id = " + str(requestPayload["id"]))
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            #print(mycursor.rowcount)
            return jsonify({'message': str(mycursor.rowcount) + "record(s) updated"})




api.add_resource(Hello, "/hello")
api.add_resource(employee, "/employee/")

docs.register(Hello)
docs.register(employee)

# driver function
if __name__ == "__main__":
    app.run(debug=True)
