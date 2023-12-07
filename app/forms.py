from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import InputRequired
from flask_wtf.file import FileRequired, FileAllowed
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, FileField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from flask_wtf.file import FileRequired, FileAllowed


class LoginForm(FlaskForm):
    email = StringField('email', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])
    

class MessageForm(FlaskForm):
    message = StringField('message', validators=[DataRequired(message='Enter a message')])

class RegisterForm(FlaskForm):
    firstname = StringField('firstname', validators=[InputRequired()])
    lastname = StringField('lastname', validators=[InputRequired()])
    email = StringField('email', validators=[InputRequired()])
    password = PasswordField('password', validators=[InputRequired()])

class UploadForm(FlaskForm):
    title = StringField('title', validators=[DataRequired(message='All fields are required'), Length(max=255)])
    composer = StringField('composer', validators=[DataRequired(message='All fields are required'), Length(max=255)])
    genre = StringField('genre', validators=[DataRequired(message='All fields are required'), Length(max=255)])
    instrument = StringField('instrument', validators=[DataRequired(message='All fields are required'), Length(max=255)])
    file = FileField('image', validators=[
        FileRequired(),
        FileAllowed(['pdf'], 'Pdf files only!')])