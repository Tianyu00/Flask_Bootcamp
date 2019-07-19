import os
from flask import Flask, render_template, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField

app = Flask(__name__)
app.config['SECRET_KEY'] = 'key'
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'flask_database_data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
Migrate(app,db)


# models #
class Puppy(db.Model):
    __tablename__='puppies'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.Text)
    owner = db.relationship('Owner', backref='puppy', uselist=False)
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        # if self.owner:
        return f"Puppy name: {self.name}, Owner: {self.owner.name}"
        # else:
        #     print(f"Puppy name: {self.name}, Owner: {self.owner}")
class Owner(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name = db.Column(db.Text)
    puppy_id = db.Column(db.Integer,db.ForeignKey('puppies.id'))
    def __init__(self, name, puppy_id):
        self.name=name
        self.puppy_id=puppy_id

# form #
class Add(FlaskForm):
    name = StringField('puppy name:')
    submit = SubmitField('submit')
class Del(FlaskForm):
    id = IntegerField('puppy id:')
    submit = SubmitField('submit')
class Own(FlaskForm):
    id = IntegerField('puppy id:')
    name = StringField('owner name:')
    submit = SubmitField('submit')

# web page #
@app.route('/')
def index():
    return render_template('home.html')

@app.route('/add',methods=['GET','POST'])
def add():
    form = Add()
    if form.validate_on_submit():
        name=form.name.data
        db.session.add(Puppy(name))
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('add.html',form=form)

@app.route('/del',methods=['GET','POST'])
def delete():
    form = Del()
    if form.validate_on_submit():
        id=form.id.data
        puppy = Puppy.query.get(id)
        db.session.delete(puppy)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('del.html',form=form)

@app.route('/list')
def list():
    puppies = Puppy.query.all()
    return render_template('list.html',puppies=puppies)

@app.route('/own',methods=['GET','POST'])
def own():
    form = Own()
    if form.validate_on_submit():
        id=form.id.data
        owner_name = form.name.data
        db.session.add(Owner(name=owner_name,puppy_id=id))
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('own.html',form=form)

if __name__ == '__main__':
    app.run(debug=True)
