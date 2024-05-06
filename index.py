from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# SQLite Database Initialization
conn = sqlite3.connect('products.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS products
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
           title TEXT,
           description TEXT,
           price REAL)''')
conn.commit()

# Helper function
def get_product_by_id(product_id):
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products WHERE id=?", (product_id,))
    product = c.fetchone()
    conn.close()
    return product

# API Endpoints
@app.route('/products', methods=['GET'])
def get_all_products():
    page = int(request.args.get('page', 1))  # Default page is 1
    limit = int(request.args.get('limit', 5))  # Default limit is 5

    offset = (page - 1) * limit

    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("SELECT * FROM products LIMIT ? OFFSET ?", (limit, offset))    # Querying database with pagination
    products = c.fetchall()
    conn.close()

    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = get_product_by_id(product_id)
    if product:
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

@app.route('/products', methods=['POST'])
def create_product():
    data = request.json
    title = data.get('title')
    description = data.get('description')
    price = data.get('price')

    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("INSERT INTO products (title, description, price) VALUES (?, ?, ?)", (title, description, price))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product created successfully'})

@app.route('/products/<int:product_id>', methods=['PUT'])
def update_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    data = request.json
    title = data.get('title', product[1])
    description = data.get('description', product[2])
    price = data.get('price', product[3])

    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("UPDATE products SET title=?, description=?, price=? WHERE id=?", (title, description, price, product_id))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product updated successfully'})

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    product = get_product_by_id(product_id)
    if not product:
        return jsonify({'error': 'Product not found'}), 404
    
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute("DELETE FROM products WHERE id=?", (product_id,))
    conn.commit()
    conn.close()

    return jsonify({'message': 'Product deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
