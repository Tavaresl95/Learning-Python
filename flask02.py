import datetime

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    now = datetime.datetime.now()
    tavs = now.month == 3 and now.day == 25
    return render_template("tavs.html", tavs=tavs)
