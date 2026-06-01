package models

import (
	"time"
)

// Order represents the Order model - Model layer in MVC pattern
type Order struct {
	ID              uint      `json:"id" gorm:"primaryKey;autoIncrement"`
	OrderNumber     string    `json:"order_number" gorm:"unique;not null;index" binding:"required"`
	CustomerName    string    `json:"customer_name" gorm:"not null" binding:"required"`
	CustomerEmail   string    `json:"customer_email" gorm:"not null" binding:"required,email"`
	ProductName     string    `json:"product_name" gorm:"not null" binding:"required"`
	Quantity        int       `json:"quantity" gorm:"not null;default:1" binding:"required,min=1"`
	UnitPrice       float64   `json:"unit_price" gorm:"not null" binding:"required,gt=0"`
	TotalPrice      float64   `json:"total_price" gorm:"not null"`
	Status          string    `json:"status" gorm:"not null;default:'PENDING'"`
	ShippingAddress string    `json:"shipping_address" gorm:"not null" binding:"required"`
	Notes           string    `json:"notes"`
	CreatedAt       time.Time `json:"created_at"`
	UpdatedAt       time.Time `json:"updated_at"`
}

// ValidStatuses lists all allowed order statuses
var ValidStatuses = []string{"PENDING", "PROCESSING", "SHIPPED", "DELIVERED", "CANCELLED"}

// CalculateTotal sets TotalPrice = Quantity * UnitPrice
func (o *Order) CalculateTotal() {
	o.TotalPrice = float64(o.Quantity) * o.UnitPrice
}

// IsValidStatus checks if the given status string is valid
func IsValidStatus(status string) bool {
	for _, s := range ValidStatuses {
		if s == status {
			return true
		}
	}
	return false
}
