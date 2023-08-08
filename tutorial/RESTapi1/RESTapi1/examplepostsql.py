from crypt import methods
from datetime import date
import re
from readline import insert_text
from sys import is_finalizing
from flask import Flask, Jsonify, request
import mysql.connector
app =Flask(__name__)
 
mydb =mysql.connector.connect (
    host ="sql6.freesqldatabase.com"
    user ="sql6635679"
    password ="Kt8TDZLfni"
    database ="sql6635679"

) 

mycursor =mydb.cursor()

@app.route("/", methods =["GET"])
def home():
    if request.method =="GET":
        data = "server starting"
        return Jsonify({"data":data})
@app.route("/student", methods =["GET" , "POST"])
def getstudent():
    if request.method =="GET":
        mycursor.execute("SELECT"*from user_details")
        myresult = mycursor.fetchall()                 
        return Jsonify({"date":myresult})

    if request.methods =="POST":
    requestpayload =request.get_Json()
    print(requestpayload)
    print(requestpayload["userid"])

    sql="INSERT INTO user_details(user_id, username) VALUES(%s,%s)"
    val=(requestpayload["userid"],requestpayload["name"])
       mycursor.execute(sql,val)
       mydb.commit()
       return Jsonify({"data":str(mycursor.rowcount)+"record inserted."}).201
 @app.route("/student", methods =["POST"])
 def insertstudent():
 #    requestpayload =request.get_Json()
      print(requestpayload)
      print(requestpayload["userid"])
    sql="INSERT INTO user_details(user_id, username) VALUES(%s,%s)"
    val=(requestpayload["userid"],requestpayload["name"])
       mycursor.execute(sql,val)
       mydb.commit()
       return Jsonify({"data":str(mycursor.rowcount)+"record inserted."})


    if__name__=="__mani__":
      app.run(debug=True)
      
   

