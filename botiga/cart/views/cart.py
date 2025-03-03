from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Cart
from ..serializers import CartSerializer
from order.models import Order, OrderItem

@api_view(["GET"])
def get_all_carts(request):
    carts = Cart.objects.all()
    serializer = CartSerializer(carts, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_cart(request, id: int):
    try:
        cart = Cart.objects.get(id=id)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = CartSerializer(cart)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_cart(request):
    serializer = CartSerializer(request.data)
    if not serializer.is_valid(): return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    serializer.save()
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
def delete_cart(request, id: int):
    try:
        cart = Cart.objects.get(id=id)
        cart.delete()
        return Response({"message": "Cart deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["POST"])
def create_order_from_cart(request, id: int):
    try:
        cart = Cart.objects.get(id=id)
    except Cart.DoesNotExist:
        return Response({"error": "Cart not found"}, status=status.HTTP_404_NOT_FOUND)
    
    user = cart.user
    items = cart.cartitem_set.all()

    if not items.exists():
        return Response({"error": "Cart is empty"}, status=status.HTTP_400_BAD_REQUEST)

    order = Order.objects.create(user=user)

    order_items = [
        OrderItem(order=order, product=item.product, quantity=item.quantity)
        for item in items
    ]
    OrderItem.objects.bulk_create(order_items)
    items.delete()

    return Response({"message": "Order created", "order_id": order.id}, status=status.HTTP_201_CREATED)

