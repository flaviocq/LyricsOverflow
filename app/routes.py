from flask import render_template, flash, redirect, url_for
from app import app, analyze
from app.forms import SearchForm


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Carlos'}
    posts = [
        {
            'artist': 'John',
            'body': {'unique_words': '19827'}
        },

        {
            'artist': 'Bill',
            'body': {'unique_words': '56263'}
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)


@app.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if (form.validate_on_submit()):
        try:
            flash('Search requested for artist {}'.format(form.artist.data))

            artist_name, unique_word_count, genre, top_fifteen, ego_rating, total_lyrics = \
                analyze.analyze_artist(form.artist.data)
            return render_template('results.html', title='Results', artist_name=artist_name,
                            unique_word_count=unique_word_count,
                            genre=genre, top_fifteen=top_fifteen,
                            ego_rating=ego_rating, error=False)
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