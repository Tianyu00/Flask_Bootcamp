# create entries into the tables
from flask_model import db, Puppy, Owner, Toy


rufus = Puppy('rufus')
fido = Puppy('fido')
db.session.add_all([rufus, fido])
print(Puppy.query.all())                # Puppy is the name of that CLASS, or model, or table

rufus = Puppy.query.filter_by(name='rufus').first()
# rufus = Puppy.query.filter_by(name='rufus').all()[0]
# create owner
jose = Owner('jose', rufus.id)
# toys
t1 = Toy('chew toy', rufus.id)
t2 = Toy('ball', rufus.id)

db.session.add_all([jose,t1,t2])
db.session.commit()

rufus = Puppy.query.filter_by(name='rufus').first()
print(rufus)
rufus.report_toys()
