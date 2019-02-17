from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    artist = StringField('Enter an artist name here', validators=[DataRequired()])
    submit = SubmitField('Search and Analyze')
