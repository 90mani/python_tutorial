# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request

# creating a Flask app
app = Flask(__name__)

# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        data = "server starting"
        return jsonify({"data": data})


@app.route("/product", methods=["GET", "POST"])
def product():
    if request.method == "GET":
        print(request.get_json())
        data = {"itemName": "Rice", "Price": 1200, "Quantity": "25kg"}
        return jsonify({"data": data})
    if request.method == "POST":
        print(request.get_json())
        data = {"message": "Inserted successfully"}
        return jsonify({"data": data}), 201


@app.route("/list", methods=["GET", "POST"])
def list():
    if request.method == "GET":
        data = [
            {"itemName": "Rice", "Price": 1200, "Quantity": "25kg"},
            {"itemName": "Uruttu dhal", "Price": 60, "Quantity": "1kg"},
            {"itemName": "Sun flower Oil", "Price": 170, "Quantity": "1ltr"},
        ]
        return jsonify({"data": data})


@app.route("/isAvailable", methods=["GET", "POST"])
def isavilable():
    if request.method == "GET":
        data = {"message": "yes"}
        return jsonify({"data": data})


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
