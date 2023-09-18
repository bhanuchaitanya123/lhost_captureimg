from flask import Flask
from flask import redirect
from flask import url_for
from flask import render_template
from flask import request
from flask import session
import pyttsx3 as p
from  flask_sqlalchemy import SQLAlchemy
from tkinter import *

app=Flask(__name__)


@app.route("/home")
def home():
    '''s="hello"
    k=[1,2,3]
    s1=len(k)
    import math
    p = [3, 3]
    q = [6, 12]
    m=math.dist(p, q)'''
    
    return f"complete"
@app.route("/login",methods=["POST","GET"])
def login():
    if(request.method=="POST"):
        u=request.form["nm"]
        global a
        import mysql.connector
        mydb=mysql.connector.connect(host="localhost",password="mysql123456",database="car_rent",port="3306",user="root",auth_plugin='mysql_native_password')
        c=mydb.cursor()
        kpo="insert into imageid(username) values(%s)"
        klp=([u])
        c.execute(kpo,klp)
        mydb.commit()
        a=['don','rowdy','mafia']
        return redirect(url_for("user"))
    else:
        global k
        g='gangsters'
        k=['don','rowdy','mafia']
        return render_template("onclick.html",con=k,f=g)
@app.route("/imgg",methods=["POST","GET"])
def imgg():
    from werkzeug.utils import secure_filename
    import os
    import urllib.request

    FILES_DIR= 'C:\\Users\\munab\\OneDrive\\python\\static\\Uploads'
    if(request.method=="POST"):
        files=request.files.getlist('files[]')
        for file in files:
          fi=secure_filename(file.filename)
          file.save(os.path.join(FILES_DIR,fi))
        return f"upload successfully"
    else:
      return render_template("htt.html")
    
   

if __name__=="__main__":
    app.run(debug=True, port=5000, host='0.0.0.0')

#,port=5000, host='0.0.0.0'

