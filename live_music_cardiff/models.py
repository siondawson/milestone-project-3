from live_music_cardiff import db


class Users(UserMixin, db.Model):
    # schema for User model
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(250), unique=True, nullable=False)
    password = db.Column(db.String(250), nullable=False)

# initalize app with extension
db.init_app(app)

# Create database within app context

with app.app_context():
    db.create_all()


# Creates a user loader callback that returns the user object given an id
@login_manager.user_loader
def loader_user(user_id):
	return Users.query.get(user_id)
