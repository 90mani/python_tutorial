# using flask_restful
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from apispec import APISpec
from marshmallow import Schema, fields
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_apispec.views import MethodResource
from flask_apispec import marshal_with, doc, use_kwargs

# creating the flask app
app = Flask(__name__)
# creating an API object
api = Api(app)

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


# making a class for a particular resource
# the get, post methods correspond to get and post requests
# they are automatically mapped by flask_restful.
# other methods include put, delete, etc.


class Hello(MethodResource, Resource):
    # corresponds to the GET request.
    # this function is called whenever there
    # is a GET request for this resource
    @doc(description="It's my first get hello api", tags=["Hello API"])
    # @marshal_with(AwesomeResponseSchema)
    def get(self):
        return jsonify({"data": "hello world"})

    # Corresponds to POST request
    # @doc(description="It's my first post  hello api", tags=["Hello API"])
    # def post(self):
    #     data = request.get_json()  # status code
    #     return jsonify({"data": data}), 201


# another resource to calculate the square of a number
class Square(MethodResource, Resource):
    @doc(description="It's my first sqaure api", tags=["Sqaure API"])
    def get(self, num):
        return jsonify({"square": num**2})


# adding the defined resources along with their corresponding urls
api.add_resource(Hello, "/hello")
api.add_resource(Square, "/square/<int:num>")

docs.register(Hello)
docs.register(Square)
# driver function
if __name__ == "__main__":
    app.run(debug=True)
