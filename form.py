from flask import Flask, flash, render_template, request, session, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, DateTimeField,
                    RadioField, SelectField, TextField,
                    TextAreaField,SubmitField)
from wtforms.validators import DataRequired

app = Flask(__name__)

# have form, so need this
app.config['SECRET_KEY'] = 'mysecretkey'

# # form
# class InfoForm(FlaskForm):
#     breed = StringField('what breed are you')
#     submit = SubmitField('submit')
# @app.route('/',methods=['GET', 'POST'])
# def index():
#     breed = False
#     form = InfoForm()
#     if form.validate_on_submit():
#         breed = form.breed.data
#         form.breed.data = ''
#     return render_template('form_home.html', form=form, breed=breed)


# # form field
# class InfoForm(FlaskForm):
#     breed = StringField('what breed are you?', validators=[DataRequired()])
#     neutered = BooleanField('have you been neutered?')
#     mood = RadioField('please choose your mood:', choices=[('mood_one','happy'),
#                                                             ('mood_two','excited')])
#     food_choice = SelectField(u'pick your favourite food:',
#                             choices=[('chi','chicken'),('bf','beef'),('fish','fish')])
#     feedback = TextAreaField()
#     submit = SubmitField('submit')
# @app.route('/',methods=['GET', 'POST'])
# def index():
#     form = InfoForm()
#     if form.validate_on_submit(): # this will be run when user submits the form,
#                                 # so 2 returns
#         session['breed'] = form.breed.data
#         session['neutered'] = form.neutered.data
#         session['mood'] = form.mood.data
#         session['food'] = form.food_choice.data
#         session['feedback'] = form.feedback.data
#         return redirect(url_for('thankyou'))
#     return  render_template('form_field_1.html', form=form)
# @app.route('/thankyou')
# def thankyou():
#     return render_template('form_field_2.html')


# # form alert
# class SimpleForm(FlaskForm):
#     submit = SubmitField('click me')
# @app.route('/',methods=['GET', 'POST'])
# def index():
#     form = SimpleForm()
#     if form.validate_on_submit():
#         flash('you just clicked the button!')
#         flash('flash message 2')
#         return redirect(url_for('index'))
#     return render_template('form_alert.html', form=form)


# form alert 2
class SimpleForm(FlaskForm):
    breed = StringField('what breed are you?')
    submit = SubmitField('submit')
@app.route('/',methods=['GET', 'POST'])
def index():
    form = SimpleForm()
    if form.validate_on_submit():
        session['breed'] = form.breed.data
        # words = "you have changed your breed to " + session['breed']
        # flash(words)
        flash(f"you just changed your breed to: {session['breed']}")
        return redirect(url_for('index'))
    return render_template('form_alert2.html', form=form)



if __name__ == '__main__':
    app.run(debug=True)
