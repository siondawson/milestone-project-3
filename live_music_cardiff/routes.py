from flask import render_template, request, flash, redirect, url_for
from datetime import datetime, date
from live_music_cardiff import app, db
from live_music_cardiff.models import Event, User
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user, LoginManager  # noqa

login = LoginManager(app)


@login.user_loader
def load_user(id):
    '''
    Returns current user id as integer.
    '''
    return User.query.get(int(id))


@app.route("/")
def home():
    '''
    Renders home page. Sets the user as current user.
    '''
    return render_template("home.html", user=current_user)


@app.route("/sign_up", methods=['GET', 'POST'])
def sign_up():
    '''
    Allows user to sign up. Takes information requested from user on form and
    adds to 'User' table of the database.
    Flash messaged in place to alert user to a series of possible errors with
    information supplied.
    Password requested twice and compared to ensure user has entered correctly.
    '''
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
                  category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters', category='error')
        else:
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1,
                                                            method='sha256'))
            db.session.add(new_user)
            db.session.commit()
            user = User.query.filter_by(email=email).first()
            login_user(user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('home'))
    return render_template("sign_up.html", user=current_user)


@app.route('/signin', methods=['GET', 'POST'])
def login():
    '''
    Allows user to log in. User enters email. This is checked again first
    matching record in database.
    User enters password and is checked again hashed password in database.
    Flash messages in place to alert user to
     errors with their login credentials.
    '''
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
    '''
    Logs user out.
    Once user is logged out they are redirected to the login page.
    '''
    logout_user()
    return redirect(url_for('login'))


@app.route('/add_event', methods=["GET", "POST"])
@login_required
def add_event():
    '''
    Allows user to add an event. Checks if request method is "POST".
    Takes info provided by user in form and commits to the database.
    Flash message to alert user the event has been added.
    User redirected to user_events page.
    '''
    if request.method == "POST":
        event = Event(
            title=request.form.get("title"),
            venue=request.form.get("venue"),
            postcode=request.form.get("postcode"),
            description=request.form.get("description"),
            date=request.form.get("date"),
            time=request.form.get("time"),
            user_id=current_user.id)
        print(request.form.get("time"))
        db.session.add(event)
        db.session.commit()
        flash('Event Added!', category='success')

        return redirect(url_for('user_events'))
    return render_template("add_event.html", user=current_user)


@app.route('/all_events')
def all_events():
    """
    Sets variable of 'today' to the current time.
    Lists all events created by all users.
    Past events are filtered out and now shown.
    """
    today = datetime.now()
    event = list(Event.query.filter(Event.date >= today).order_by(
                            Event.date).all())
    return render_template("all_events.html", user=current_user, event=event)


@app.route('/user_events/')
def user_events():
    """
    Lists all events that the logged in user has created.
    """
    users_events = Event.query.order_by(Event.date).filter_by(
                            user_id=current_user.id)
    return render_template("user_events.html", user=current_user,
                           user_events=users_events)


@app.route("/edit_event/<int:event_id>", methods=["GET", "POST"])
def edit_event(event_id):
    """
    Allows user to edit event.
    Sets user variable to current user.
    Queries database for event_id.
    Pre populates form with information from database ready for editing.
    """
    user = current_user
    user_event = Event.query.get_or_404(event_id)
    if user_event.user_id == user.id:
        if request.method == "POST":
            user_event.title = request.form.get("title")
            user_event.venue = request.form.get("venue")
            user_event.postcode = request.form.get("postcode")
            user_event.description = request.form.get("description")
            user_event.date = request.form.get("date")
            user_event.time = request.form.get("time")
            db.session.commit()
            return redirect(url_for("user_events"))
        return render_template("edit_event.html", user_event=user_event,
                               user=current_user)
    flash('You do not have permission to edit this event', category='error')
    return render_template('home.html', user=current_user)


@app.route("/delete_event/<int:event_id>")
def delete_event(event_id):
    '''
    Function for deleting events.
    If statement checks if user id matches the foreign key user_id
    of event before deletion.
    If user id matches the events user id foreign key, the event is deleted.
    If it does not match the user is alerted that they may not
    delete the event as it does not belong to them.
    '''
    user_event = Event.query.get_or_404(event_id)
    user = current_user
    if user_event.user_id == user.id:
        db.session.delete(user_event)
        db.session.commit()
        return redirect(url_for("user_events"))
    flash('You do not have permission to delete this event', category='error')
    return render_template('home.html', user=current_user)


@app.route("/event/<int:event_id>")
def event(event_id):
    '''
    Takes event id as integer allowing database to be queried for this event
    so that event data may be displayed on the front end.
    '''
    current_event = Event.query.get_or_404(event_id)
    return render_template("event.html", event=current_event,
                           user=current_user)
