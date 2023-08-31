from live_music_cardiff import db


class User(db.Model):
    # schema for User model
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        # __repr__ to represent itself in form of a string
        return self



class Event(db.Model):
    # schema for Event model
    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
        # __repr__ to represent itself in form of a string
        return self
