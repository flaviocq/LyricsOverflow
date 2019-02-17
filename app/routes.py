from flask import render_template, flash, redirect, url_for
from app import app, analyze, models, db, getImage
from app.forms import SearchForm


@app.route('/')
@app.route('/index')
def index():
    posts = models.Artist.query.all()[:5]
    return render_template('index.html', title='Home', posts=posts)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if (form.validate_on_submit()):
        try:
            artist_name, unique_word_count, genre, top_fifteen, ego_rating, total_lyrics = \
                analyze.analyze_artist(form.artist.data)
            flash('Search successful!')
            img = getImage.get_lastFM_info(artist_name)
            artist_info = models.Artist(name=artist_name, unique_word_count=unique_word_count,
                                        narcissism_rating=ego_rating, genre=genre, img_url=img)
            test_artist_info = models.Artist.query.filter_by(name=artist_name).first()
            if test_artist_info is None:
                db.session.add(artist_info)
                db.session.commit()
            return render_template('results.html', title='Results', artist_name=artist_name,
                                   unique_word_count=unique_word_count,
                                   genre=genre, top_fifteen=top_fifteen,
                                   ego_rating=ego_rating, error=False, img=img)
        except IndexError:
            return render_template('search.html', title='Search', form=form, error=True)
    return render_template('search.html', title='Search', form=form, error=False)


@app.route('/results', methods=['GET', 'POST'])
def results(artist_name, unique_word_count, genre, top_fifteen, ego_rating, total_lyrics):
    return render_template('results.html', title='Results', artist_name=artist_name,
                           unique_word_count=unique_word_count,
                           genre=genre, top_fifteen=top_fifteen,
                           ego_rating=ego_rating)


'''
    - add list to base html file to display at the bottom somehow
    - add timestamps to artist entries for sorting at bottom
    - create results html and route/render
    - 
'''
