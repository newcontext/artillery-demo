""" Simple authenticated api """
import json
from flask import Flask, request, jsonify, make_response
from flask_jwt_extended import (
    JWTManager, jwt_required, create_access_token,
    get_jwt_identity
)


users = []

with open('users.json') as file:
    users = json.load(file)


def verify_login(username, password):
    # compare user/password combo to json file

    for user in users: 
        if user['username'] == username and user['password'] == password:
            return user    
    else:
        return None


def jwt_identity(payload):
    print(payload)
    user_id = payload['identity']
    print(user_id)
    return user_details(user_id)


def user_details(user_id):
    # return user details based on id
    for user in users:
        if user['id'] == user_id or user['username'] == user_id:
            return user
    else:
        return None


def verify_token(token):
    # bugbug: security issue
    # intentionally obtuse way of checking the token
    # just checks if it exists and not whether token
    # is allowed to retrieve user

    for user in users: 
        if user['id'] == token:
            token = user['id']
            return token    
    else:
        return None


application = Flask(__name__)
application.config['SECRET_KEY'] = 'my-secret-key'
application.config['JWT_SECRET_KEY'] = 'also-my-secret-key'
jwt = JWTManager(application)


@application.route('/')
def index():
    return jsonify({"msg": "Simple API"})


@application.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username:
        return jsonify({"msg": "Missing username parameter"}), 400
        
    if not password:
        return jsonify({"msg": "Missing password parameter"}), 400

    valid_user = verify_login(username, password)

    if valid_user:
        access_token = create_access_token(identity=username)
        return jsonify(id=valid_user['id'], access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@application.route('/logout')
def logout():
    return jsonify({"msg": "Bye"})


@application.route('/user/<user_id>')
@jwt_required
def details(user_id):
    details = user_details(user_id)
    if details:
        current_user = get_jwt_identity()
        if details['username'] == current_user:
            return jsonify(details), 200
        else:
            return jsonify({"msg": "Not authorized"}), 403
    else:
        return jsonify({"msg": "Not found"}), 404


if __name__ == "__main__":
    application.run(port=5000, debug=True)