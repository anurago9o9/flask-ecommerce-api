from flask import Flask, jsonify
from flask_jwt import JWT, jwt_required, current_identity
from werkzeug.security import safe_str_cmp
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('JWT_SECRET_KEY')

users = {
    'username': {'password': 'password'}
}

# JWT setup
def authenticate(username, password):
    user = users.get(username, None)
    if user and safe_str_cmp(user['password'], password):
        return user

def identity(payload):
    user_id = payload['identity']
    return users.get(user_id)

jwt = JWT(app, authenticate, identity)

@app.route('/protected')
@jwt_required()
def protected():
    return jsonify(logged_in_as=current_identity)

if __name__ == '__main__':
    app.run(debug=True)
