from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('password', validators=[DataRequired()])
    submit = SubmitField('Log in')


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(),Email()])
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired(),EqualTo('pass_confirm'),message = 'passwords must match'])
    pass_confirm = PasswordField('confirm password', validators=[DataRequired()])
    def check_email(self,field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('your email has been registered')
    def check_email(self,field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken')
