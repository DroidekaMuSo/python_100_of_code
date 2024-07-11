from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField, FloatField
from wtforms.validators import DataRequired, URL


class ADDMOVIE(FlaskForm):
    title = StringField(label='Title', name="title", validators=[DataRequired()])
    year = IntegerField(label='Year', name="year", validators=[DataRequired()])
    description = StringField(label='Description', name="description", validators=[DataRequired()])
    rating = FloatField(label='Rating', name="rating", validators=[DataRequired()])
    ranking = FloatField(label='Ranking', name="ranking", validators=[DataRequired()])
    review = StringField(label='Review', name="review", validators=[DataRequired()])
    img_url = StringField(label='Img URL', name="img_url", validators=[DataRequired(), URL()])

    submit = SubmitField(label='Submit')

class SELECTMOVIE(FlaskForm):
    title = StringField(label='Movie Title', name="title", validators=[DataRequired()])
    submit = SubmitField(label='Look Up')


class EDITMOVIE(FlaskForm):
    rating = FloatField(label='Your rating out of 10', name="new_rating", validators=[DataRequired()])
    review = StringField(label='Your review', name="new_review", validators=[DataRequired()])
    submit = SubmitField(label='Update')
