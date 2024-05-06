# Flask E-commerce API

This is a RESTful API built with Flask for managing products in an e-commerce application.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/anurago9o9/flask-ecommerce-api.git
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory and add your JWT secret key:

   ```bash
   JWT_SECRET_KEY=your_jwt_secret_key_here
   ```

4. Run the Flask app:
   ```bash
   python run.py
   ```

## Endpoints

### GET /products

Retrieves a list of all products.

### GET /products/{id}

Retrieves details of a specific product by its ID.

### POST /products

Creates a new product with details like title, description, price, etc. (data should be received in JSON format).

Example request body:

```json
{
  "title": "Product Title",
  "description": "Product Description",
  "price": 19.99
}
```

### PUT /products/{id}

Updates an existing product based on its ID.

Example request body:

```json
{
  "title": "Updated Product Title",
  "description": "Updated Product Description",
  "price": 24.99
}
```

### DELETE /products/{id}

Deletes a product by its ID.

## Authentication

This API uses JWT authentication. To access protected endpoints, include a valid JWT token in the request headers:

```
Authorization: Bearer your_jwt_token_here


```
