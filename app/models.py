from app import db

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    unique_word_count = db.Column(db.Integer())
    narcissism_rating = db.Column(db.Integer())
    genre = db.Column(db.String(64), index=True, unique=False)

    def __repr__(self):
        return '<Artist {}: {}>'.format(self.name, self.unique_word_count)


class WordInfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(64), index=True, unique=True)
    freq = db.Column(db.Integer)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))

    def __repr__(self):
        return '<Word {}>'.format(self.word)
