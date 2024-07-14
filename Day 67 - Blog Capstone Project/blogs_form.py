from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, URL


class ADD_POST(FlaskForm):
    title = StringField(label='Title', name="title", validators=[DataRequired()])
    subtitle = StringField(label='Subtitle', name="subtitle", validators=[DataRequired()])
    author = StringField(label='Author', name="author", validators=[DataRequired()])
    img_url = StringField(label='Img URL', name="img_url", validators=[DataRequired(), URL()])
    body = TextAreaField(label='Body', name="body", validators=[DataRequired()])
    submit = SubmitField(label='Submit')
