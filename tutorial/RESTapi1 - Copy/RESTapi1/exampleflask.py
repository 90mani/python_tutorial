#using flask to make an api
#import necessary libraries an a function
#from flask import Flask, Jsonify, request

#creating a Flask app
app = Flask(__name__)
#on the terminal type:curl http://127.0.0.1:5000/
#return hello world world when we use GET
#return the data that we send when we use Post
@app.route("/", methods = ["GET"])
def home():
    if request.method == "GET":
    data = "server started"
    return Jsonify({"data":data})
@app.route("/student", methods = ["GET"])
def getstudent():
    if request.method == "GET":
        data = [
            {"name": "Charu", "class":"A", "school":"GGHS"}
            {"name": "Anu", "class":"B", "school":"GGHS"}
            {"name": "Abi", "class":"C", "school":"GGHS"}
                ]
#data = {"name": "Charu", "class":"A", "school":"GGHS"}
return Jsonify({"data": "data"})
@app.route("/student/" methods = ["GET"])
def getStudentAndLeaves():
    #data =[
    #  {"name": "Charu", "class":"A", "school":"GGHS"}
    #  {"name": "Anu", "class":"B", "school":"GGHS"}
    #  {"name": "Abi", "class":"C", "school":"GGHS"}
    #]
    #result = ""
    #for x in data:
    if class == x["class"]:
        return jsonify ({"data":"class"})
    #return jsonify({"data":result})
    #a sample function to calculate the square of a number
    #the number to be squared is sent in the URL when we use GET
    #on the teriminal type :curl http://127.0.1:5000/home/10
    #this returns 100 (squre of 10)
    @app.route ("/home/<int:num>", methods = ["GET"])
    def disp(num):
        return jsonify({"data": num**2})
    #driver function
    if__name__ = "__Abi__":
    app.run(debug=True)
     
