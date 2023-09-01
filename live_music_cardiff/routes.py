from flask import render_template
from live_music_cardiff import app, db


@app.route("/")
def home():
    return render_template("home.html")


@app.route('/register', methods=["GET", "POST"])
def register():
    # If the user made a POST request. create a new user
    if request.method == "POST":
        user = Users(username=request.form.get("username"), 
                    password=request.form.get("password"))
        # Add the user to the database
        db.session.add(user)
        # Commit the changes made
        db.session.commit()
        # Once the user account is created, redirect them
        # to login route
        return redirect(url_for("login"))
    return render_template("sign_up.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    # If a post request was made, find the user by
    # filtering for the username
    if request.method == "POST":
        user = Users.query.filter_by(
            username=request.form.get("username")).first()
        # Check if the password entered is the
        # same as the user's password
        if user.password == request.form.get("password"):
            # Use the login_user method to log in the user
            login_user(user)
            return redirect(url_for("home"))
        # Redirect the user back to the home
        # (we'll create the home route in a moment)
    return render_template("login.html")
