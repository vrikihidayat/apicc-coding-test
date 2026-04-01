#!/usr/bin/env python3
"""
Seed script to populate the database with sample orders
Run this script after starting the Flask app at least once to create the database.
"""
from app import app, db
from models import Order
from decimal import Decimal


def seed_sample_orders():
    """Create sample orders in the database"""
    
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
    
    with app.app_context():
        # Check if orders already exist
        existing_orders = Order.query.filter(
            Order.order_number.in_([order['order_number'] for order in sample_orders])
        ).count()
        
        if existing_orders > 0:
            print(f"⚠️  Found {existing_orders} existing sample orders.")
            response = input("Do you want to delete them and recreate? (y/N): ")
            if response.lower() == 'y':
                Order.query.filter(
                    Order.order_number.in_([order['order_number'] for order in sample_orders])
                ).delete()
                db.session.commit()
                print("✓ Deleted existing sample orders")
            else:
                print("Cancelled. No changes made.")
                return
        
        # Create sample orders
        created_count = 0
        for order_data in sample_orders:
            order = Order(**order_data)
            db.session.add(order)
            created_count += 1
        
        db.session.commit()
        
        print(f"\n✅ Successfully created {created_count} sample orders!")
        print("\nSample orders by status:")
        print("  - 3 PENDING orders")
        print("  - 2 PROCESSING orders")
        print("  - 2 SHIPPED orders")
        print("  - 2 DELIVERED orders")
        print("  - 1 CANCELLED order")
        print("\nYou can now test the API endpoints with this data.")


if __name__ == '__main__':
    print("="*60)
    print("Flask Order Management - Database Seeder")
    print("="*60)
    print()
    seed_sample_orders()
    print()
    print("="*60)#!/usr/bin/env python3
"""
Seed script to populate the database with sample orders
Run this script after starting the Flask app at least once to create the database.
"""
from app import app, db
from models import Order
from decimal import Decimal


def seed_sample_orders():
    """Create sample orders in the database"""
    
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
    
    with app.app_context():
        # Check if orders already exist
        existing_orders = Order.query.filter(
            Order.order_number.in_([order['order_number'] for order in sample_orders])
        ).count()
        
        if existing_orders > 0:
            print(f"⚠️  Found {existing_orders} existing sample orders.")
            response = input("Do you want to delete them and recreate? (y/N): ")
            if response.lower() == 'y':
                Order.query.filter(
                    Order.order_number.in_([order['order_number'] for order in sample_orders])
                ).delete()
                db.session.commit()
                print("✓ Deleted existing sample orders")
            else:
                print("Cancelled. No changes made.")
                return
        
        # Create sample orders
        created_count = 0
        for order_data in sample_orders:
            order = Order(**order_data)
            db.session.add(order)
            created_count += 1
        
        db.session.commit()
        
        print(f"\n✅ Successfully created {created_count} sample orders!")
        print("\nSample orders by status:")
        print("  - 3 PENDING orders")
        print("  - 2 PROCESSING orders")
        print("  - 2 SHIPPED orders")
        print("  - 2 DELIVERED orders")
        print("  - 1 CANCELLED order")
        print("\nYou can now test the API endpoints with this data.")


if __name__ == '__main__':
    print("="*60)
    print("Flask Order Management - Database Seeder")
    print("="*60)
    print()
    seed_sample_orders()
    print()
    print("="*60)