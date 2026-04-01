from flask import request
from flask_restful import Resource
from database import db
from models import Order
from decimal import Decimal


class OrderListResource(Resource):
    def get(self):
        orders = Order.query.order_by(Order.created_at.desc()).all()
        return {'orders': [order.to_dict() for order in orders]}, 200
    
    def post(self):
        data = request.get_json()
        required_fields = ['order_number', 'customer_name', 'customer_email', 
                          'product_name', 'quantity', 'unit_price', 'shipping_address']
        for field in required_fields:
            if field not in data:
                return {'error': f'Missing required field: {field}'}, 400
        
        if data['quantity'] < 1:
            return {'error': 'Quantity must be at least 1'}, 400
        
        if float(data['unit_price']) <= 0:
            return {'error': 'Unit price must be greater than 0'}, 400
        
        order = Order(
            order_number=data['order_number'],
            customer_name=data['customer_name'],
            customer_email=data['customer_email'],
            product_name=data['product_name'],
            quantity=data['quantity'],
            unit_price=Decimal(str(data['unit_price'])),
            shipping_address=data['shipping_address'],
            notes=data.get('notes', ''),
            status=data.get('status', 'PENDING')
        )
        order.calculate_total()
        
        try:
            db.session.add(order)
            db.session.commit()
            return {'order': order.to_dict()}, 201
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400


class OrderResource(Resource):
    def get(self, order_id):
        order = Order.query.get_or_404(order_id)
        return {'order': order.to_dict()}, 200
    
    def put(self, order_id):
        order = Order.query.get_or_404(order_id)
        data = request.get_json()
        
        if 'customer_name' in data:
            order.customer_name = data['customer_name']
        if 'customer_email' in data:
            order.customer_email = data['customer_email']
        if 'product_name' in data:
            order.product_name = data['product_name']
        if 'quantity' in data:
            order.quantity = data['quantity']
        if 'unit_price' in data:
            order.unit_price = Decimal(str(data['unit_price']))
        if 'status' in data:
            order.status = data['status']
        if 'shipping_address' in data:
            order.shipping_address = data['shipping_address']
        if 'notes' in data:
            order.notes = data['notes']
        
        order.calculate_total()
        
        try:
            db.session.commit()
            return {'order': order.to_dict()}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400
    
    def patch(self, order_id):
        return self.put(order_id)
    
    def delete(self, order_id):
        order = Order.query.get_or_404(order_id)
        try:
            db.session.delete(order)
            db.session.commit()
            return {'message': 'Order deleted successfully'}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400


class OrderCancelResource(Resource):
    def post(self, order_id):
        order = Order.query.get_or_404(order_id)
        if order.status in ['DELIVERED', 'CANCELLED']:
            return {'error': 'Cannot cancel order with current status'}, 400
        order.status = 'CANCELLED'
        try:
            db.session.commit()
            return {'order': order.to_dict()}, 200
        except Exception as e:
            db.session.rollback()
            return {'error': str(e)}, 400


class PendingOrdersResource(Resource):
    def get(self):
        orders = Order.query.filter_by(status='PENDING').order_by(Order.created_at.desc()).all()
        return {'orders': [order.to_dict() for order in orders]}, 200
