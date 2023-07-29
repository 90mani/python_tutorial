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


@app.route("/customer", methods=["GET"])
def getCustomer():
    if request.method == "GET":
        data = {"Name": "rani", "A/c number": 101, "balance": 15000}
        return jsonify({"data": data})


@app.route("/loans", methods=["GET"])
def getLoans():
    if request.method == "GET":
        data = {"totalLoan": 50, "approved": 20, "pending": 40}
        return jsonify({"data": data})


@app.route("/customer/loan", methods=["GET"])
def getCustomerloan():
    if request.method == "GET":
        data = [
            {
                "ac_number": 10001,
                "Name": "jeevi",
                "balance": 3000,
                "loan_number": [
                    {"loanAc_number": "ABC001", "loanAmount": 100000, "type": "PL"},
                    {"loanAc_number": "ABC001", "loanAmount": 100000, "type": "HL"},
                ],
                "duration": "6 month",
                "payable": "not pay",
            },
            {
                "ac_number": 10002,
                "Name": "kayal",
                "balance": 10000,
                "loan_number": [
                    {"loanAc_number": "ABC001", "loanAmount": 100000, "type": "PL"},
                    {"loanAc_number": "ABC001", "loanAmount": 100000, "type": "HL"},
                ],
                "duration": "2 month",
                "payable": "pay",
            },
        ]

        return jsonify({"data": data})


@app.route("/customer/loan/status", methods=["GET"])
def getCustomerstatus():
    if request.method == "GET":
        data = {"Name": "rose", "A/c number": 202, "message": "in active"}

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
