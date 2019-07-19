from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'
hashed_password = bcrypt.generate_password_hash(password=password)

check = bcrypt.check_password_hash(hashed_password,'wrongpassword')
# print(check)
check = bcrypt.check_password_hash(hashed_password,'supersecretpassword')
# print(check)


from werkzeug.security import generate_password_hash, check_password_hash
hashed_password = generate_password_hash('mypassword')
print(hashed_password)
check = check_password_hash(hashed_password,'wrongpassword')
print(check)
check = check_password_hash(hashed_password,'mypassword')
print(check)
