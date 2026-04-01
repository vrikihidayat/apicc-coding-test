from django.contrib import admin
from .models import Order


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_number', 'customer_name', 'product_name', 'quantity', 'total_price', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('order_number', 'customer_name', 'customer_email', 'product_name')
    readonly_fields = ('total_price', 'created_at', 'updated_at')
    ordering = ('-created_at',)