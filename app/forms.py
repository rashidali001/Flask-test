from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired



class LoginForm(FlaskForm):
    username = StringField("username", validators=[DataRequired()])
    password = PasswordField("Password...", validators=[DataRequired()])
    remember = BooleanField("Remember me", validators=[DataRequired()])
    submit = SubmitField("Login")