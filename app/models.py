from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    unique_word_count = db.Column(db.Integer())

    def __repr__(self):
        return '<Artist {}'.format(self.name)
