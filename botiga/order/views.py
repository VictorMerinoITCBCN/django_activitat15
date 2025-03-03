from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializers import OrderSerializer
from .models import StatusChoices

def not_completed_orders():
    return Order.objects.exclude(stauts=StatusChoices.DELIVERED)

@api_view(["GET"])
def get_all_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_not_completed_orders(request):
    orders = not_completed_orders()
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["DELETE"])
def delete_not_completed_orders(request):
    orders = not_completed_orders()
    orders.delete()
    return Response({"message": "Orders deleted successfully"}, status=status.HTTP_204_NO_CONTENT)