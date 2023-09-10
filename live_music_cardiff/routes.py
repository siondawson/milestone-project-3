from flask import render_template, request, flash, redirect, url_for
from live_music_cardiff import app, db
from live_music_cardiff.models import Event, User
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager  # noqa

login = LoginManager(app)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route("/")
def home():
    user = current_user
    return render_template("home.html", user=current_user)


@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('Email already exists', category='error')
        elif len(email) < 4:
            flash('Email must be greater than 3 characters.', category='error')
        elif len(first_name) < 2:
            flash('First name must be greater than 1 characters.',
                    category='error')  # noqa
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name, password=generate_password_hash(password1, method='sha256'))  # noqa
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('home'))
    return render_template("sign_up.html", user=current_user)


@app.route('/signin', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        print(email)
        password = request.form.get('password1')

        user = User.query.filter_by(email=email).first()
        
        if user:
            print(user.password)
            print(password)
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('home'))
            else:
                flash('Incorrect password, try again', category='error')
        else:
            flash('Email does not exist.', category='error')
    return render_template("login.html", user=current_user)


@app.route('/signout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/add_event', methods=["GET", "POST"])
@login_required
def add_event():
    print(current_user.id)
    if request.method == "POST":
        event = Event(
            title=request.form.get("title"),
            venue=request.form.get("venue"),
            postcode=request.form.get("postcode"),
            description=request.form.get("description"),
            date=request.form.get("date"),
            user_id=current_user.id)
        print(event.title)
        db.session.add(event)
        db.session.commit()
        flash('Event Added!', category='success')

        return redirect(url_for('user_events'))
    return render_template("add_event.html", user=current_user)


@app.route('/all_events')
def all_events():
    event = list(Event.query.order_by(Event.title).all())
    return render_template("all_events.html", user=current_user, event=event)


@app.route('/user_events')
def user_events():
    user_events = Event.query.order_by(Event.title).filter_by(user_id=current_user.id)
    return render_template("user_events.html", user=current_user, user_events=user_events)


@app.route("/edit_event/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    user_event = Event.query.get_or_404(event_id)
    if request.method == "POST":
        user_event.title = request.form.get("title")
        user_event.venue = request.form.get("venue")
        user_event.postcode = request.form.get("postcode")
        user_event.description = request.form.get("description")
        user_event.date = request.form.get("date")
        db.session.commit()
        return redirect(url_for("user_events"))
    return render_template("edit_event.html", user_event=user_event, user=current_user) #user=current_user goes here not at top of function


@app.route("/delete_event/<int:event_id>")
def delete_event(event_id):
    user_event = Event.query.get_or_404(event_id)
    print(user_event)
    db.session.delete(user_event)
    db.session.commit()
    return redirect(url_for("user_events"))
