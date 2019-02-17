from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    unique_word_count = db.Column(db.Integer())
    narcissism_rating = db.Column(db.DECIMAL())
    genre = db.Column(db.String(64), index=True, unique=False)

    def __repr__(self):
        return '<Artist {}>'.format(self.name)
