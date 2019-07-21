from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms import ValidationError
from flask_wtf.file import FileField, FileAllowed

from flask_login import current_user
from myproject.models import User

class LoginForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Log in')

class RegistrationForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    username = StringField('username',validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),
                    EqualTo('pass_confirm',message='password must match')])
    pass_confirm = PasswordField('confirm password', validators=[DataRequired()])
    submit=SubmitField('register')
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('your email has been registered already')
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('your username has been registered already')

class UpdateUserForm(FlaskForm):
    email = StringField('email',validators=[DataRequired(),Email()])
    username = StringField('username',validators=[DataRequired()])
    picture = FileField('update profile picture', validators=[FileAllowed(['jpg','png'])])
    submit = SubmitField('Update')
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('your email has been registered already')
    def check_username(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('your username has been registered already')
