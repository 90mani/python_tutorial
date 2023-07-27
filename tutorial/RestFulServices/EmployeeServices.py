# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "Server started"
        return jsonify({"data": data})


@app.route("/employees", methods=["GET"])
def getEmployee():
    if request.method == "GET":
        data = [
            {"name": "John", "id": 1001, "email": "test@gmail.com"},
            {"name": "Ravi", "id": 1002, "email": "test1@gmail.com"},
            {"name": "Mani", "id": 1003, "email": "test2@gmail.com"},
        ]
        # data = {"name": "John", "id": 1001, "email": "test@gmail.com"}
        return jsonify({"data": data})


@app.route("/employee/<int:id>", methods=["GET"])
def getEmployeeAndLeaves():
    # data = [
    #     {"name": "John", "id": 1001, "email": "test@gmail.com"},
    #     {"name": "Ravi", "id": 1002, "email": "test1@gmail.com"},
    #     {"name": "Mani", "id": 1003, "email": "test2@gmail.com"},
    # ]
    # result = ""
    # for x in data:
    #     if id == x["id"]:
    return jsonify({"data": id})


# return jsonify({"data": result})


# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route("/home/<int:num>", methods=["GET"])
def disp(num):
    return jsonify({"data": num**2})


# driver function
if __name__ == "__main__":
    app.run(debug=True)
