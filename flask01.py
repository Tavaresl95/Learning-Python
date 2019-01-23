from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    good = "Python is great!"
    return render_template("index.html", good=good)
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return ("Hello, {}! Deu certo!".format(name))

#SET FLASK_APP=flask01.py
#python -m flask run