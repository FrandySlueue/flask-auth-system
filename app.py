from flask import Flask
from flask_cors import CORS
from redis_client import redis_client


app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
   return { "message": "Welcome to the Sign-in Registration API!" }, 200


if __name__ == '__main__':
   app.run(debug=True)
