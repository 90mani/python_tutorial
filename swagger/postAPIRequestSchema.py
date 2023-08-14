from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs


# import mysql.connector


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

# mydb = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="2003@saran",
#     database="employee_mgnt",
# )
# mycursor = mydb.cursor()


class StudentReuqetBody(Schema):
    name = fields.String(required=True, description="Student name")
    rolNo = fields.Int(required=True, description="Student rolNo")


class StudentsReuqetBody(Schema):
    students = fields.List(fields.Nested(StudentReuqetBody))


class Hello(MethodResource, Resource):
    @doc(description="It's my first get hello api", tags=["Hello API"])
    def get(self):
        return jsonify({"data": "hello world"})


class student(MethodResource, Resource):
    @doc(description="get student data", tags=["Student"])
    def get(self):
        if request.method == "GET":
            # mycursor.execute("SELECT * from employee")
            # myresult = mycursor.fetchall()
            return jsonify({"data": "***********"})

    @doc(description="get student data", tags=["Student"])
    @use_kwargs(StudentsReuqetBody, location=("json"))
    # @marshal_with(AwesomeResponseSchema)  # marshalling
    def post(self, **kwargs):
        if request.method == "POST":
            print("entered into post method")
            requestPayload = request.get_json()
            print(type(requestPayload))
            print(type(requestPayload["students"]))
            val = None
            for x in requestPayload["students"]:
                val = ()

            # print(requestPayload)
            # print(requestPayload["userId"])
            # sql = "INSERT INTO employee (employee_id,name,password,phone_number,experiance) VALUES (%s,%s,%s,%s,%s)"
            # val = (
            #     requestPayload["userId"],
            #     requestPayload["u_name"],
            #     requestPayload["passcode"],
            #     requestPayload["number"],
            #     requestPayload["no_experiance"],
            # ),(
            # )
            # mycursor.execute(sql, val)
            # mydb.commit()
            # return (jsonify({"data": str(mycursor.rowcount) + "record inserted"}),)
            return jsonify({"data": "Post api executed"})


api.add_resource(Hello, "/hello")
api.add_resource(student, "/student")


docs.register(Hello)
docs.register(student)

if __name__ == "__main__":
    app.run(debug=True)