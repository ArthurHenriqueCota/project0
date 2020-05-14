from flask import Flask,render_template

app=Flask(__name__)

@app.route("/")

def homepage():
    return render_template("homepage.html")

@app.route("/prophylaxis.html")

def prophylaxis():
    return render_template("prophylaxis.html")