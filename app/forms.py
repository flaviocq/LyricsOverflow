from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    artist = StringField('Artist Name', validators=[DataRequired()])
    submit = SubmitField('Search and Analyze')
