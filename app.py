"""
    Account Service:
    Håndterer brugerkonti, herunder registrering, autentificering og profiladministration.
    Behandler login, logout, passwordhåndtering og brugerroller.
"""
from flask import Flask, jsonify, request, make_response
import requests
import sqlite3

app = Flask(__name__)

data = requests.get('https://dummyjson.com/products/')
products = data.json()['products']

def connect_db():
    conn = sqlite3.connect('products.db')
    return conn

def create_table():
    conn = connect_db()
    conn.execute('''CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    category TEXT,
    price REAL,
    stock INTEGER,
    brand TEXT,
    sku TEXT,
    weight REAL,
    image_url TEXT,
    thumbnail_url TEXT
);''')
    conn.commit()
    conn.close()

def insert_products(products):
    conn = connect_db()
    cursor = conn.cursor()

    for product in products:
        cursor.execute('''INSERT OR REPLACE INTO products 
            (id, title, description, category, price, stock, brand, sku, weight, image_url, thumbnail_url) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
            (
                product.get('id'), 
                product.get('title'), 
                product.get('description'), 
                product.get('category'), 
                product.get('price'), 
                product.get('stock'), 
                product.get('brand', ''), 
                product.get('sku'),   
                product.get('weight', 0),  
                product['images'][0],      
                product.get('thumbnail', '')
            )
        )
    conn.commit()
    conn.close()


create_table()
insert_products(products)



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
def get_all_product():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()
    conn.close()
    
    product_list = []
    for product in products:
        product_list.append({
            'id': product[0],
            'title': product[1],
            'description': product[2],
            'category': product[3],
            'price': product[4],
            'stock': product[5],
            'brand': product[6], 
            'sku': product[7],
            'weight': product[8],
            'image_url': product[9],
            'thumbnail_url': product[10]
        })
    return jsonify(product_list), 200

@app.route('/product/<int:id>', methods=['GET'])
def get_product_by_id(id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE id=?',(id,))
    products = cursor.fetchall()
    conn.close()
    
    product_list = []
    for product in products:
        product_list.append({
            'id': product[0],
            'title': product[1],
            'description': product[2],
            'category': product[3],
            'price': product[4],
            'stock': product[5],
            'brand': product[6], 
            'sku': product[7],
            'weight': product[8],
            'image_url': product[9],
            'thumbnail_url': product[10]
        })
    return jsonify(product_list), 200

@app.route('/product/category/<string:category>', methods=['GET'])
def get_product_by_category():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM products WHERE category=?',(category,))
    products = cursor.fetchall()
    conn.close()
    
    product_list = []
    for product in products:
        product_list.append({
            'id': product[0],
            'title': product[1],
            'description': product[2],
            'category': product[3],
            'price': product[4],
            'stock': product[5],
            'brand': product[6], 
            'sku': product[7],
            'weight': product[8],
            'image_url': product[9],
            'thumbnail_url': product[10]
        })
    return jsonify(product_list), 200

app.run(debug=True, host='0.0.0.0')
