# flask_database_setupdatabase.py
from flask_database import db, Puppy
db.create_all() # create all columns
sam = Puppy('Sammy',3)
frank = Puppy('Frankie',4)
print(sam.id) # haven't add to database, should see 'none'
print(frank.id)
db.session.add_all([sam, frank])
db.session.commit() # save change to database
print(sam.id)
print(frank.id)

# flask_database_crud.py (run after flask_database_setupdatabase.py)
# CRUD: create, read, delete
from flask_database import db, Puppy
## create ##
my_puppy = Puppy('Rufus', 5)
db.session.add(my_puppy)
db.session.commit()
## read ##
all_puppies = Puppy.query.all()
print(all_puppies)
# select by ID
puppy_one = Puppy.query.get(1)
print(puppy_one.name)
# filter
puppy_frankie = Puppy.query.filter_by(name='Frankie')
print(puppy_frankie.all())
## update ##
first_puppy = Puppy.query.get(1)
first_puppy.age = 10
db.session.add(first_puppy)
db.session.commit()
## delete ##
second_puppy = Puppy.query.get(2)
db.session.delete(second_puppy)
db.session.commit()

all_puppies = Puppy.query.all()
print(all_puppies)
