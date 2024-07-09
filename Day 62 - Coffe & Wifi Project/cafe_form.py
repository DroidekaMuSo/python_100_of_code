from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, TimeField
from wtforms.validators import DataRequired, URL


class CafeForm(FlaskForm):
    cafe = StringField(label='Cafe name', validators=[DataRequired()])
    location_url = StringField(label='Location', validators=[DataRequired(), URL()])
    open_time = TimeField(label='Open', format='%H:%M', validators=[DataRequired()])
    close_time = TimeField(label='Close', format='%H:%M', validators=[DataRequired()])

    coffee_rating = SelectField(label='Coffee',
                                choices=["", "☕️", "☕️☕️", "☕️☕️☕️", "☕️☕️☕️☕️", "☕️☕️☕️☕️☕️"],
                                validators=[DataRequired()])
    wifi_rating = SelectField(label='Wifi',
                              choices=["", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
                              validators=[DataRequired()])
    power_rating = SelectField(label='Power',
                               choices=["", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
                               validators=[DataRequired()])

    submit = SubmitField(label='Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------
