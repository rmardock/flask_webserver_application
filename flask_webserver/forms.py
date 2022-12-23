# Form Classes 
from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    StringField,
    SubmitField,
    PasswordField,
)

from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    
    username = StringField('Username', [DataRequired()])
    password = PasswordField('Password', [DataRequired()])
    login = SubmitField("Login")