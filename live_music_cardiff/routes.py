from flask import render_template, request
from live_music_cardiff import app, db


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
     return render_template("sign_up.html")
      

@app.route('/login', methods=['GET', 'POST'])
def login():
    return render_template("login.html", boolean=True)


@app.route('/logout')
def logout():
    return "<p>Logout</>"
