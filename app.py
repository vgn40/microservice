"""
    Account Service:
    Håndterer brugerkonti, herunder registrering, autentificering og profiladministration.
    Behandler login, logout, passwordhåndtering og brugerroller.
"""

from flask import Flask, jsonify, request, make_response
import requests

app = Flask(__name__)

# DATABASE - skal skiftes til sqlite
users_db = []
data = requests.get('https://dummyjson.com/users/1')
users_db.append(data.json())

# find bruger via username
def find_user_by_username(username):
    return next((user for user in users_db if user['username'] == username), None)

# Register en ny bruger
@app.route('/profile', methods=['POST'])
def register():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({'message': 'Username and password are required'}), 400

    if find_user_by_username(username):
        return jsonify({'message': 'User already exists'}), 400

    new_user = {
        "id": len(users_db) + 1,
        "username": username,
        "password": password,
    }

    users_db.append(new_user) 
    return jsonify({'message': f'User registered successfully'}), 201

@app.route('/profile', methods=['GET'])
def view_profile():
    data = request.headers.get('Authorization')
    if not data:
        return jsonify({'message': 'User not logged in'}), 401

    user = find_user_by_username(data)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(users_db), 200

@app.route('/profile', methods=['PUT'])
def edit_profile():
    return jsonify(), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    user = find_user_by_username(username)

    if user and user['password'] == password:
        # komponer et response
        response = make_response(jsonify({'message': f'Login successful'}), 200)
        response.headers['Authorization'] = username
        return response
    
    return jsonify({'message': 'Invalid username or password'}), 401

@app.route('/logout', methods=['POST'])
def logout():
    return jsonify(), 201

@app.route('/product', methods=['GET'])
def get_product():
    data = request.headers.get('Authorization')
    if not data:
        return jsonify({'message': 'User not logged in'}), 401

    user = find_user_by_username(data)
    if not user:
        return jsonify({'message': 'User not found'}), 404

    return jsonify(users_db), 200


app.run(debug=True, host='0.0.0.0')