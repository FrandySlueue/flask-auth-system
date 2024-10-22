from pymongo import MongoClient
from flask_bcrypt import Bcrypt


client = MongoClient('mongodb://localhost:27017/')
db = client['user_db']
users = db['users']
bcrypt = Bcrypt()

def create_user(username, password):
   hashed_pw = bcrypt.generate_password_hash(password).decode('utf-8')
   users.insert_one({ "username": username })