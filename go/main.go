package main

import (
	"log"

	"order-api/database"
	"order-api/models"
	"order-api/routes"
)

func main() {
	// Initialize database (Model)
	database.ConnectDatabase()

	// Auto-migrate models
	database.DB.AutoMigrate(&models.Order{})

	// Setup router (Controller + Routes)
	r := routes.SetupRouter()

	// Start server
	log.Println("Server running on http://localhost:8080")
	if err := r.Run(":8080"); err != nil {
		log.Fatal("Failed to start server:", err)
	}
}
