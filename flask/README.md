# Flask Order Management API

Flask-RESTful boilerplate SQLite database.

## Structure

- **Model**: `models.py` - Order data model
- **Controller**: `controllers/order_controller.py` - API resources
- **View**: Flask-RESTful handles JSON responses

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application
```bash
python app.py
```

3. Populate database with sample data:
```bash
python seed_data.py
```


## API Endpoints
- **GET /api/orders** - List all orders
- **POST /api/orders** - Create new order
- **GET /api/orders/{id}** - Retrieve order
- **PUT /api/orders/{id}** - Update order
- **PATCH /api/orders/{id}** - Partial update
- **DELETE /api/orders/{id}** - Delete order
- **POST /api/orders/{id}/cancel** - Cancel order
- **GET /api/orders/pending** - List pending orders