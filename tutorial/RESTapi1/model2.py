# A simple function to calculate the square of a number
# the number to be squared is sent in the URL when we use GET
# on the terminal type: curl http://127.0.0.1:5000 / home / 10
# this returns 100 (square of 10)
@app.route("/employee", methods=["GET"])
def getEmployee():
    return jsonify({"name": "John", "age": 30, "city": "New York"})


@app.route("/employee/name", methods=["GET"])
def getEmployeeByName():
    return jsonify({"name": "John"})


@app.route("/employee/all", methods=["GET"])
def getEmployeeAllInfo():
    return jsonify(
        {
            "name": "John",
            "age": 30,
            "married": True,
            "divorced": False,
            "children": ("Ann", "Billy"),
            "pets": None,
            "cars": [
                {"model": "BMW 230", "mpg": 27.5},
                {"model": "Ford Edge", "mpg": 24.1},
            ],
        }
    )


# driver function
if _name_ == "_main_":
    app.run(debug=True)


