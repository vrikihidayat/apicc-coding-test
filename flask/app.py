from flask import Flask
from flask_restful import Api
from database import db
import os

# Initialize Flask app
app = Flask(__name__)

# Configuration
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(basedir, "orders.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your-secret-key-change-in-production'

# Initialize extensions with app
db.init_app(app)
api = Api(app)

# Import models after db initialization
import models

# Import controllers after models
from controllers.order_controller import OrderListResource, OrderResource, OrderCancelResource, PendingOrdersResource

# Register API routes
api.add_resource(OrderListResource, '/api/orders')
api.add_resource(OrderResource, '/api/orders/<int:order_id>')
api.add_resource(OrderCancelResource, '/api/orders/<int:order_id>/cancel')
api.add_resource(PendingOrdersResource, '/api/orders/pending')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Create tables
    app.run(debug=True)
