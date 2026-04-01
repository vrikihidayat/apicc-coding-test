from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer


class OrderViewSet(viewsets.ModelViewSet):
    """
    Order ViewSet - Controller layer in MVC pattern
    
    Provides CRUD operations:
    - list: GET /api/orders/
    - create: POST /api/orders/
    - retrieve: GET /api/orders/{id}/
    - update: PUT /api/orders/{id}/
    - partial_update: PATCH /api/orders/{id}/
    - destroy: DELETE /api/orders/{id}/
    """
    
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    
    @action(detail=True, methods=['post'])
    def cancel(self, request, pk=None):
        """Custom action to cancel an order"""
        order = self.get_object()
        if order.status in ['DELIVERED', 'CANCELLED']:
            return Response(
                {'error': 'Cannot cancel order with current status'},
                status=status.HTTP_400_BAD_REQUEST
            )
        order.status = 'CANCELLED'
        order.save()
        serializer = self.get_serializer(order)
        return Response(serializer.data)
    
    @action(detail=False, methods=['get'])
    def pending(self, request):
        """Get all pending orders"""
        pending_orders = self.queryset.filter(status='PENDING')
        serializer = self.get_serializer(pending_orders, many=True)
        return Response(serializer.data)