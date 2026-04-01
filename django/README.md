# Django Order Management API

Django REST Framework boilerplate with SQLite database.

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

3. Create superuser
```bash
python manage.py createsuperuser
```

4. Run server:
```bash
python manage.py runserver
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