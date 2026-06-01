# Go Order Management API

Gin + GORM boilerplate following MVC design pattern with SQLite database.

## Structure

```
go/
├── main.go                      # Entry point
├── database/database.go         # DB connection (Model infrastructure)
├── models/order.go              # Order model (Model layer)
├── controllers/order_controller.go  # HTTP handlers (Controller layer)
├── routes/routes.go             # Route definitions (View layer)
├── seed/seed.go                 # Sample data seeder
└── go.mod                       # Module definition
```

## Setup

1. Install Go (1.21+): https://go.dev/dl/

2. Install dependencies:
```bash
go mod tidy
```

3. Run the server:
```bash
go run main.go
```

4. (Optional) Seed sample data:
```bash
go run seed/seed.go
```

## API Endpoints

- `GET    /api/orders`          - List all orders
- `POST   /api/orders`          - Create new order
- `GET    /api/orders/:id`      - Get order by ID
- `PUT    /api/orders/:id`      - Update order
- `PATCH  /api/orders/:id`      - Partial update
- `DELETE /api/orders/:id`      - Delete order
- `POST   /api/orders/:id/cancel` - Cancel order
- `GET    /api/orders/pending`  - List pending orders

## Example Request

```bash
curl -X POST http://localhost:8080/api/orders \\
  -H "Content-Type: application/json" \\
  -d '{
    "order_number": "ORD-001",
    "customer_name": "John Doe",
    "customer_email": "john@example.com",
    "product_name": "Product A",
    "quantity": 2,
    "unit_price": 29.99,
    "shipping_address": "123 Main St, City, Country"
  }'
```

## Database

SQLite (`orders.db`) - automatically created on first run.
