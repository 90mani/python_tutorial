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
    host="127.0.0.1",
    user="root",
    password="2003@saran",
    database="employee_mgnt",
)
mycursor = mydb.cursor()


class StudentReuqetBody(Schema):
    userId = fields.Int(required=False, description="employee id")
    u_name = fields.String(required=False, description="employee name")
    passcode = fields.String(required=False, description="employee name")
    number = fields.Int(required=False, description="employee name")


class StudentdeleteReuqetBody(Schema):
    userid= fields.Int(required=True, description="employee_id")

class studentUpdateReuqetBody(Schema):
    u_name = fields.String(required=True, description="employee Name")
    id = fields.Int(required=False, description="employee id")



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
            sql = "INSERT INTO employee (employee_id,name,password,phone_number) VALUES (%s,%s,%s,%s)"
            val = (userId, name, passcode, number)
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

class deletestudent(MethodResource, Resource):
    @doc(description="delete single data", tags=["Employee"])
    @use_kwargs(StudentdeleteReuqetBody, location=("json"))
    def delete(self,**kwargs):
        if request.method == "DELETE":
            requestPayload = request.get_json()
            userid=requestPayload["userid"]
            sql = "DELETE FROM employee WHERE employee_id = " + str(requestPayload["userid"])
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            print(mycursor.rowcount)
            return jsonify({"data": str(mycursor.rowcount) + "record(s) deleted"})
        
    @doc(description="employee update data", tags=["Employee"])
    @use_kwargs(studentUpdateReuqetBody, location=("json"))
    def put (self, **kwargs):
        if request.method == "PUT":
            requestPayload = request.get_json()
            u_name = requestPayload["u_name"]
            id= requestPayload["id"]
            sql =("UPDATE employee SET name = '" + str(requestPayload["u_name"]) +"' WHERE employee_id = " + str(requestPayload["id"]))
            print(sql)
            mycursor.execute(sql)
            mydb.commit()
            #print(mycursor.rowcount)
            return jsonify({'message': str(mycursor.rowcount) + "record(s) updated"})   
        
       # u_name = fields.String(required=True, description="employee Name")
    #number = fields.Int(required=False, description="employee name")



api.add_resource(student, "/employee")
api.add_resource(SearchStudent, "/employee/<int:id>")
api.add_resource(deletestudent, "/employee")

docs.register(student)
docs.register(SearchStudent)
docs.register(deletestudent)

if __name__ == "__main__":
    app.run(debug=True)