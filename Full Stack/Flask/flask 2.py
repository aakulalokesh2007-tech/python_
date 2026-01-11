from flask import Flask,redirect,url_for
app=Flask(__name__)
@app.route("/")
def home():
    return "this is the main page <h1>okk<h1>"
@app.route("/<name>")
def user(name):
    return f"hello {name}!"
@app.route("/admin")
def admin():
    return redirect(url_for("user",name="lokesh"))
@app.route("/no/")#thih cant be use by the user but can work by deloper
def no():
    return redirect(url_for("user",name="yessss"))



app.run()