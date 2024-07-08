from flask_wtf import FlaskForm
from wtforms import PasswordField, EmailField, SubmitField
from wtforms.validators import DataRequired, Length, Email



class MyForm(FlaskForm):
    email = EmailField(label='Email', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8)])
    submit = SubmitField(label="Log In")
