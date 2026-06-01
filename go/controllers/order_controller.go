package controllers

import (
	"net/http"
	"strconv"

	"github.com/gin-gonic/gin"
	"order-api/database"
	"order-api/models"
)

// ListOrders handles GET /api/orders
func ListOrders(c *gin.Context) {
	var orders []models.Order
	if err := database.DB.Order("created_at DESC").Find(&orders).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"orders": orders})
}

// CreateOrder handles POST /api/orders
func CreateOrder(c *gin.Context) {
	var order models.Order
	if err := c.ShouldBindJSON(&order); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	if order.Status == "" {
		order.Status = "PENDING"
	}

	if !models.IsValidStatus(order.Status) {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid status value"})
		return
	}

	order.CalculateTotal()

	if err := database.DB.Create(&order).Error; err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusCreated, gin.H{"order": order})
}

// GetOrder handles GET /api/orders/:id
func GetOrder(c *gin.Context) {
	order, ok := findOrderByID(c)
	if !ok {
		return
	}
	c.JSON(http.StatusOK, gin.H{"order": order})
}

// UpdateOrder handles PUT and PATCH /api/orders/:id
func UpdateOrder(c *gin.Context) {
	order, ok := findOrderByID(c)
	if !ok {
		return
	}

	var input map[string]interface{}
	if err := c.ShouldBindJSON(&input); err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": err.Error()})
		return
	}

	if status, exists := input["status"]; exists {
		if !models.IsValidStatus(status.(string)) {
			c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid status value"})
			return
		}
	}

	if err := database.DB.Model(&order).Updates(input).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}

	// Recalculate total if quantity or unit_price changed
	if _, qOk := input["quantity"]; qOk {
		order.CalculateTotal()
		database.DB.Save(&order)
	} else if _, pOk := input["unit_price"]; pOk {
		order.CalculateTotal()
		database.DB.Save(&order)
	}

	c.JSON(http.StatusOK, gin.H{"order": order})
}

// DeleteOrder handles DELETE /api/orders/:id
func DeleteOrder(c *gin.Context) {
	order, ok := findOrderByID(c)
	if !ok {
		return
	}
	if err := database.DB.Delete(&order).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"message": "Order deleted successfully"})
}

// CancelOrder handles POST /api/orders/:id/cancel
func CancelOrder(c *gin.Context) {
	order, ok := findOrderByID(c)
	if !ok {
		return
	}
	if order.Status == "DELIVERED" || order.Status == "CANCELLED" {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Cannot cancel order with current status"})
		return
	}
	order.Status = "CANCELLED"
	if err := database.DB.Save(&order).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"order": order})
}

// GetPendingOrders handles GET /api/orders/pending
func GetPendingOrders(c *gin.Context) {
	var orders []models.Order
	if err := database.DB.Where("status = ?", "PENDING").Order("created_at DESC").Find(&orders).Error; err != nil {
		c.JSON(http.StatusInternalServerError, gin.H{"error": err.Error()})
		return
	}
	c.JSON(http.StatusOK, gin.H{"orders": orders})
}

// findOrderByID is a helper to fetch an order by :id param
func findOrderByID(c *gin.Context) (models.Order, bool) {
	id, err := strconv.Atoi(c.Param("id"))
	if err != nil {
		c.JSON(http.StatusBadRequest, gin.H{"error": "Invalid order ID"})
		return models.Order{}, false
	}
	var order models.Order
	if err := database.DB.First(&order, id).Error; err != nil {
		c.JSON(http.StatusNotFound, gin.H{"error": "Order not found"})
		return models.Order{}, false
	}
	return order, true
}
