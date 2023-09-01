from flask import render_template
from live_music_cardiff import app, db


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sign_up")
def sign_up():
    return render_template("sign_up.html")


@app.route("/login")
def login():
    return render_template("login.html")
