import base64
import hashlib
import random
import string
from flask import Flask,request,render_template,redirect
import jwt
import pickle

app = Flask(__name__,static_folder="static",template_folder="templates")

privateKey=open("./private.pem","rb").read()
publicKey=open("./public.pem","rb").read()
characters = string.ascii_letters + string.digits + string.punctuation
adminPassword = ''.join(random.choice(characters) for i in range(18))
user_list={"admin":adminPassword}

@app.route("/register",methods=["GET","POST"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    elif request.method=="POST":
        username=request.form.get("username")
        password=request.form.get("password")
        if (username==None)|(password==None)|(username in user_list):
            return "error"

        user_list[username]=password
        return "OK"


@app.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    elif request.method=="POST":
        username = request.form.get("username")
        password = request.form.get("password")
        if (username == None) | (password == None):
            return "error"

        if username not in user_list:
            return "please register first"

        if user_list[username] !=password:
            return "your password is not right"

        ss={"username":username,"password":hashlib.md5(password.encode()).hexdigest(),"is_admin":False}
        if username=="admin":
            ss["is_admin"]=True
            ss.update(introduction=base64.b64encode(pickle.dumps("1ou_Kn0w_80w_to_b3c0m3_4dm1n?")).decode())

        token=jwt.encode(ss,privateKey,algorithm='RS256')

        return "OK",200,{"Set-Cookie":"Token="+token.decode()}


@app.route("/admin",methods=["GET"])
def admin():
    token=request.headers.get("Cookie")[6:]
    print(token)
    if token ==None:
        redirect("login")
    try:
        real= jwt.decode(token, publicKey, algorithms=['HS256', 'RS256'])
    except Exception as e:
        print(e)
        return "error"
    username = real["username"]
    password = real["password"]
    is_admin = real["is_admin"]
    if password != hashlib.md5(user_list[username].encode()).hexdigest():
        return "Hacker!"

    if is_admin:
        serial_S = base64.b64decode(real["introduction"])
        introduction=pickle.loads(serial_S)
        return f"Welcome!!!,{username},introduction: {introduction}"
    else:
        return f"{username},you don't have enough permission in here"

@app.route("/",methods=["GET"])
def jump():
    return redirect("login")

if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0",port=80)