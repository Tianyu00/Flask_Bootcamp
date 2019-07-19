import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


basedir = os.path.abspath(os.path.dirname(__file__))
# get the abs path of the current dir

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'flask_database_data.sqlite')
                # database path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)           # these 3 lines create a database for us in python

Migrate(app, db)  # this way if we change our table here, will be reflected in database
#################################################
# python and database
class Puppy(db.Model):
    __tablename__ = 'puppies'   # default name is your CLASS name

    # attributes
    id = db.Column(db.Integer, primary_key = True)     # create a column
    name = db.Column(db.Text)
    age = db.Column(db.Integer)
    breed = db.Column(db.Text)

    # methods
    def __init__(self, name, age,breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __repr__(self):
        return f"Puppy {self.name} is {self.age} year/s old"
# go to script --> flask_database_2.py






if __name__ == '__main__':
    app.run(debug=True)
