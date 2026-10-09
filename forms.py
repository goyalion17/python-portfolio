from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Email, Length


class ContactForm(FlaskForm):
    name = StringField(validators=[DataRequired(), Length(max=80)])
    email = StringField(validators=[DataRequired(), Email(), Length(max=120)])
    message = TextAreaField(validators=[DataRequired(), Length(min=10, max=2000)])
    # Honeypot: hidden from people, bots tend to fill it in
    website = StringField()
