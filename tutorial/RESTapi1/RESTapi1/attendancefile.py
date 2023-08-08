from flask import Flask,  jsonify, request
import mysql.connector


app = Flask(__name__)

mydb = mysql.connector.connect(
    host="sql6.freesqldatabase.com",
    user="sql6636952",
    password="9JJrXbm37m",
    database="sql6636952",

)
mycursor = mydb.cursor()


@app.route("/", methods=["GET"])
def home():
    if request.method == "GET":
        data = "server starting"
        return jsonify({"data":data})
    
    @app.route("/student", methods=["GET", "POST"])
    def getstudent():
        if request.method == "GET":
            mycursor.execute("SELECT * from stu_attendance")
            myresult =mycursor.fetchall()
            return jsonify({"data": myresult})
        if request.method == "POST":
            requestpayload =request.get_Json()
            print(requestpayload)
            print(requestpayload["Roll No"])
            sql = "INSERT INTO stu_attendance (Roll No, Name, Degree, Course, Sem, attendance)VALUES(%s,%s,%s,%s,%s,%s)"
            val = (requestpayload["Roll No"],requestpayload["Name"],requestpayload["Degree"],requestpayload["Course"],requestpayload["Sem"],requestpayload["attendance"])
            mycursor.execute(sql,val)
            mydb.commit()
            return jsonify({"data": str(mycursor.rowcount)+"recordinserted."}),201
    #@app.route("/student",methods=["POST"])
    #def insertstudent():
    # requestpayload =request.get_Json()
        #print(requestpayload)
        #print(requestpayload["Roll No"])
        #sql = "INSERT INTO stu_attendance(Roll No,Name,Degree,Course,Sem,attendance)VALUES(%s,%s,%s,%s,%s,%s)"
        #val = (requestpayload["Roll No"],requestpayload["Name"]requestpayload["Degree"]requestpayload["Course"]requestpayload["Sem"]requestpayload["attendance"])
        #mycursor.execute(sql,val)
        #mydb.commit()
        #return jsonify({"data": str(mycursor.rowcount)+"recordinserted."}) 


        if __name__=="__main__":
            app.run(debug=True)
                                        