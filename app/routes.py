from flask import render_template, flash, redirect, url_for
from app import app
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
        flash('Search requested for artist {}'.format(form.artist))
        return redirect(url_for('index'))
    return render_template('search.html', title='Search', form=form)
