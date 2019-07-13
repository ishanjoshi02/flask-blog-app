from flask_wtf import Form
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.validators import DataRequired, EqualTo


class RegisterForm(Form):
    firstname = StringField('First Name', validators=[
                            DataRequired(message="First name is required")])
    lastname = StringField('Last Name', validators=[
                           DataRequired(message="Last name is required")])
    username = StringField('Username', validators=[
                           DataRequired(message="Username is required")])
    password = PasswordField('Password', validators=[
        DataRequired("Password is required"), EqualTo("confirm_password",  message='Passwords must match')])
    confirm_password = PasswordField(
        'Confirm Password', validators=[DataRequired(message="Confirm Password is required")])


class LoginForm(Form):
    username = StringField("username", validators=[
                           DataRequired(message="username is required")])
    password = PasswordField("Password", validators=[
        DataRequired("password is required")])