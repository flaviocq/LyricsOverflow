from flask import render_template, flash, redirect, url_for, request
from app import app, analyze, models, db, getImage
from app.forms import SearchForm


@app.route('/')
@app.route('/index')
def index():
    page = request.args.get('page', 1, type=int)
    posts = models.Artist.query.order_by(models.Artist.timestamp.desc()).paginate(
        page, app.config['POSTS_PER_PAGE'], False)
    next_url = url_for('index', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('index', page=posts.prev_num) \
        if posts.has_prev else None
    return render_template('index.html', title='Home', posts=posts.items, next_url=next_url, prev_url=prev_url)


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
def results(artist_name, unique_word_count, genre, top_fifteen, ego_rating):
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
