package routes

import (
	"github.com/gin-gonic/gin"
	"order-api/controllers"
)

// SetupRouter configures all API routes - View layer in MVC pattern
func SetupRouter() *gin.Engine {
	r := gin.Default()

	api := r.Group("/api")
	{
		orders := api.Group("/orders")
		{
			orders.GET("", controllers.ListOrders)
			orders.POST("", controllers.CreateOrder)
			orders.GET("/pending", controllers.GetPendingOrders)
			orders.GET("/:id", controllers.GetOrder)
			orders.PUT("/:id", controllers.UpdateOrder)
			orders.PATCH("/:id", controllers.UpdateOrder)
			orders.DELETE("/:id", controllers.DeleteOrder)
			orders.POST("/:id/cancel", controllers.CancelOrder)
		}
	}

	return r
}
