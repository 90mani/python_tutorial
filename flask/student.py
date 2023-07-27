# Using flask to make an api
# import necessary libraries and functions
from flask import Flask, jsonify, request


app = Flask(_name_)


# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "server started"
        return jsonify({"data": data})



    @app.route("/student", methods=[GET])
    def getstudent():
        if request.method == "GET":
            data = [
        
            {"id": 1001, "name": "kalai", "mark": 65,85,70, "grade": A+}

            ]
        return jsonify({"data": data})
    @app.route("/student/<int:id>", methods=["GET"])
    def getstudentmarks():
        #data = [
        #    {"id": 1001, "name": "kalai", "mark":65,85,70, "grade": A+}
        #    {"id": 1002, "name": "kamala","mark":70,80,90, "grade": A++}
        # ]
        # result = ""
        # for x in data:
        #     if id == x["id"]:
        return jsonify({"data": id})


    return jsonify({"data": result})



    
@app.route('/home/<int:num>', methods = ['GET'])
def disp(num):
  
    return jsonify({'data': num**2})
  
  
# driver function
if __name__ == "__main__":
    app.run(debug=True)
  
             

