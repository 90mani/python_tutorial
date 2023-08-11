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

app.config.update(
    {
        "APISPEC_SPEC": APISpec(
            title="student Management",
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
    password="2810",
    database="studend",
)
mycursor = mydb.cursor()


class Hello(MethodResource, Resource):
    @doc(description="It's my first get hello api", tags=["Hello API"])
    
    def get(self):
        return jsonify({"data": "hello world"})


class student(MethodResource, Resource):
    @doc(description="get student data", tags=["hi"])

    def get(student):
        if request.method == "GET":
            mycursor.execute("select* from marksheet")
            myresult = mycursor.fetchall()
            return jsonify({"data": "myresult"})
        

api.add_resource(Hello, "/hello")
api.add_resource(student, "/student")

docs.register(Hello)
docs.register(student)
# driver function
if __name__ == "__main__":
    app.run(debug=True)