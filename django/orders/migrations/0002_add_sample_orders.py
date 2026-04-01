# Generated migration for adding sample orders
from django.db import migrations
from decimal import Decimal


def create_sample_orders(apps, schema_editor):
    """Create sample orders"""
    Order = apps.get_model('orders', 'Order')
    
    sample_orders = [
        {
            'order_number': 'ORD-2026-001',
            'customer_name': 'John Doe',
            'customer_email': 'john.doe@example.com',
            'product_name': 'Wireless Headphones',
            'quantity': 2,
            'unit_price': Decimal('79.99'),
            'total_price': Decimal('159.98'),
            'status': 'PENDING',
            'shipping_address': '123 Main Street, New York, NY 10001, USA',
            'notes': 'Please deliver before 5 PM'
        },
        {
            'order_number': 'ORD-2026-002',
            'customer_name': 'Jane Smith',
            'customer_email': 'jane.smith@example.com',
            'product_name': 'Smart Watch',
            'quantity': 1,
            'unit_price': Decimal('299.99'),
            'total_price': Decimal('299.99'),
            'status': 'PROCESSING',
            'shipping_address': '456 Oak Avenue, Los Angeles, CA 90001, USA',
            'notes': 'Gift wrap requested'
        },
        {
            'order_number': 'ORD-2026-003',
            'customer_name': 'Bob Johnson',
            'customer_email': 'bob.johnson@example.com',
            'product_name': 'Laptop Stand',
            'quantity': 3,
            'unit_price': Decimal('45.00'),
            'total_price': Decimal('135.00'),
            'status': 'SHIPPED',
            'shipping_address': '789 Pine Road, Chicago, IL 60601, USA',
            'notes': ''
        },
        {
            'order_number': 'ORD-2026-004',
            'customer_name': 'Alice Williams',
            'customer_email': 'alice.williams@example.com',
            'product_name': 'Mechanical Keyboard',
            'quantity': 1,
            'unit_price': Decimal('129.99'),
            'total_price': Decimal('129.99'),
            'status': 'DELIVERED',
            'shipping_address': '321 Elm Street, Houston, TX 77001, USA',
            'notes': 'Delivered to front desk'
        },
        {
            'order_number': 'ORD-2026-005',
            'customer_name': 'Charlie Brown',
            'customer_email': 'charlie.brown@example.com',
            'product_name': 'USB-C Hub',
            'quantity': 5,
            'unit_price': Decimal('34.99'),
            'total_price': Decimal('174.95'),
            'status': 'PENDING',
            'shipping_address': '654 Maple Drive, Phoenix, AZ 85001, USA',
            'notes': 'Bulk order for office'
        },
        {
            'order_number': 'ORD-2026-006',
            'customer_name': 'Diana Prince',
            'customer_email': 'diana.prince@example.com',
            'product_name': 'Wireless Mouse',
            'quantity': 2,
            'unit_price': Decimal('25.50'),
            'total_price': Decimal('51.00'),
            'status': 'PROCESSING',
            'shipping_address': '987 Cedar Lane, Philadelphia, PA 19019, USA',
            'notes': 'Prefer black color'
        },
        {
            'order_number': 'ORD-2026-007',
            'customer_name': 'Edward Norton',
            'customer_email': 'edward.norton@example.com',
            'product_name': 'Monitor Stand',
            'quantity': 1,
            'unit_price': Decimal('89.99'),
            'total_price': Decimal('89.99'),
            'status': 'CANCELLED',
            'shipping_address': '147 Birch Street, San Antonio, TX 78201, USA',
            'notes': 'Customer requested cancellation'
        },
        {
            'order_number': 'ORD-2026-008',
            'customer_name': 'Fiona Green',
            'customer_email': 'fiona.green@example.com',
            'product_name': 'Desk Lamp',
            'quantity': 4,
            'unit_price': Decimal('39.99'),
            'total_price': Decimal('159.96'),
            'status': 'SHIPPED',
            'shipping_address': '258 Willow Court, San Diego, CA 92101, USA',
            'notes': 'Leave at doorstep'
        },
        {
            'order_number': 'ORD-2026-009',
            'customer_name': 'George Harris',
            'customer_email': 'george.harris@example.com',
            'product_name': 'Webcam HD',
            'quantity': 1,
            'unit_price': Decimal('149.99'),
            'total_price': Decimal('149.99'),
            'status': 'PENDING',
            'shipping_address': '369 Spruce Avenue, Dallas, TX 75201, USA',
            'notes': 'For home office setup'
        },
        {
            'order_number': 'ORD-2026-010',
            'customer_name': 'Helen Martinez',
            'customer_email': 'helen.martinez@example.com',
            'product_name': 'Ergonomic Chair',
            'quantity': 1,
            'unit_price': Decimal('399.99'),
            'total_price': Decimal('399.99'),
            'status': 'DELIVERED',
            'shipping_address': '741 Ash Boulevard, San Jose, CA 95101, USA',
            'notes': 'Assembly required - customer confirmed'
        }
    ]
    
    for order_data in sample_orders:
        Order.objects.create(**order_data)


def remove_sample_orders(apps, schema_editor):
    """Remove sample orders (reverse operation)"""
    Order = apps.get_model('orders', 'Order')
    order_numbers = [
        'ORD-2026-001', 'ORD-2026-002', 'ORD-2026-003', 'ORD-2026-004', 
        'ORD-2026-005', 'ORD-2026-006', 'ORD-2026-007', 'ORD-2026-008',
        'ORD-2026-009', 'ORD-2026-010'
    ]
    Order.objects.filter(order_number__in=order_numbers).delete()


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(create_sample_orders, remove_sample_orders),
    ]
