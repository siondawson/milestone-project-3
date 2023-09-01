from flask import render_template
from live_music_cardiff import app, db


@app.route("/")
def home():
    return render_template("base.html")


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")
