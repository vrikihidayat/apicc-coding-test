package main

import (
	"log"

	"order-api/database"
	"order-api/models"
)

func main() {
	// Initialize database
	database.ConnectDatabase()
	database.DB.AutoMigrate(&models.Order{})

	sampleOrders := []models.Order{
		{OrderNumber: "ORD-2026-001", CustomerName: "John Doe", CustomerEmail: "john.doe@example.com", ProductName: "Wireless Headphones", Quantity: 2, UnitPrice: 79.99, TotalPrice: 159.98, Status: "PENDING", ShippingAddress: "123 Main Street, New York, NY 10001, USA", Notes: "Please deliver before 5 PM"},
		{OrderNumber: "ORD-2026-002", CustomerName: "Jane Smith", CustomerEmail: "jane.smith@example.com", ProductName: "Smart Watch", Quantity: 1, UnitPrice: 299.99, TotalPrice: 299.99, Status: "PROCESSING", ShippingAddress: "456 Oak Avenue, Los Angeles, CA 90001, USA", Notes: "Gift wrap requested"},
		{OrderNumber: "ORD-2026-003", CustomerName: "Bob Johnson", CustomerEmail: "bob.johnson@example.com", ProductName: "Laptop Stand", Quantity: 3, UnitPrice: 45.00, TotalPrice: 135.00, Status: "SHIPPED", ShippingAddress: "789 Pine Road, Chicago, IL 60601, USA", Notes: ""},
		{OrderNumber: "ORD-2026-004", CustomerName: "Alice Williams", CustomerEmail: "alice.williams@example.com", ProductName: "Mechanical Keyboard", Quantity: 1, UnitPrice: 129.99, TotalPrice: 129.99, Status: "DELIVERED", ShippingAddress: "321 Elm Street, Houston, TX 77001, USA", Notes: "Delivered to front desk"},
		{OrderNumber: "ORD-2026-005", CustomerName: "Charlie Brown", CustomerEmail: "charlie.brown@example.com", ProductName: "USB-C Hub", Quantity: 5, UnitPrice: 34.99, TotalPrice: 174.95, Status: "PENDING", ShippingAddress: "654 Maple Drive, Phoenix, AZ 85001, USA", Notes: "Bulk order for office"},
		{OrderNumber: "ORD-2026-006", CustomerName: "Diana Prince", CustomerEmail: "diana.prince@example.com", ProductName: "Wireless Mouse", Quantity: 2, UnitPrice: 25.50, TotalPrice: 51.00, Status: "PROCESSING", ShippingAddress: "987 Cedar Lane, Philadelphia, PA 19019, USA", Notes: "Prefer black color"},
		{OrderNumber: "ORD-2026-007", CustomerName: "Edward Norton", CustomerEmail: "edward.norton@example.com", ProductName: "Monitor Stand", Quantity: 1, UnitPrice: 89.99, TotalPrice: 89.99, Status: "CANCELLED", ShippingAddress: "147 Birch Street, San Antonio, TX 78201, USA", Notes: "Customer requested cancellation"},
		{OrderNumber: "ORD-2026-008", CustomerName: "Fiona Green", CustomerEmail: "fiona.green@example.com", ProductName: "Desk Lamp", Quantity: 4, UnitPrice: 39.99, TotalPrice: 159.96, Status: "SHIPPED", ShippingAddress: "258 Willow Court, San Diego, CA 92101, USA", Notes: "Leave at doorstep"},
		{OrderNumber: "ORD-2026-009", CustomerName: "George Harris", CustomerEmail: "george.harris@example.com", ProductName: "Webcam HD", Quantity: 1, UnitPrice: 149.99, TotalPrice: 149.99, Status: "PENDING", ShippingAddress: "369 Spruce Avenue, Dallas, TX 75201, USA", Notes: "For home office setup"},
		{OrderNumber: "ORD-2026-010", CustomerName: "Helen Martinez", CustomerEmail: "helen.martinez@example.com", ProductName: "Ergonomic Chair", Quantity: 1, UnitPrice: 399.99, TotalPrice: 399.99, Status: "DELIVERED", ShippingAddress: "741 Ash Boulevard, San Jose, CA 95101, USA", Notes: "Assembly required - customer confirmed"},
	}

	created := 0
	skipped := 0
	for _, order := range sampleOrders {
		var existing models.Order
		if err := database.DB.Where("order_number = ?", order.OrderNumber).First(&existing).Error; err != nil {
			database.DB.Create(&order)
			log.Printf("Created: %s", order.OrderNumber)
			created++
		} else {
			log.Printf("Skipped (already exists): %s", order.OrderNumber)
			skipped++
		}
	}
	log.Printf("Seeding complete: %d created, %d skipped", created, skipped)
}
