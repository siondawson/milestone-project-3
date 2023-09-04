from flask import render_template, request, flash, redirect, url_for
from live_music_cardiff import app, db
from live_music_cardiff.models import Event, User
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password2')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.',
                    category='error')  # noqa
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            flash('Account created!', category='success')
            return redirect(url_for('routes.home'))
    return render_template("sign_up.html")
      

@app.route('/signin', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html", boolean=True)


@app.route('/signout')
def logout():
    return "<p>Logout</p>"
