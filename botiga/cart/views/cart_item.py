from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import CartItem
from ..serializers import CartItemSerializer

@api_view(["GET"])
def get_all_cart_items(request):
    items = CartItem.objects.all()
    serializer = CartItemSerializer(items, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["GET"])
def get_cart_item(request, id: int):
    try:
        item = CartItem.objects.get(id=id)
    except CartItem.DoesNotExist:
        return Response({"error": "CartItem not found"}, status=status.HTTP_404_NOT_FOUND)
    serializer = CartItemSerializer(item)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(["POST"])
def create_cart_item(request):
    serializer = CartItemSerializer(data = request.data)
    if not serializer.is_valid(): return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(["DELETE"])
def delete_cart_item(request, id: int):
    try:
        item = CartItem.objects.get(id=id)
        item.delete()
        return Response({"message": "CartItem deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    except CartItem.DoesNotExist:
        return Response({"error": "CartItem not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["PATCH"])
def patch_cart_item(request, id: int):
    quantity = request.data.get("quantity", None)
    if not quantity: return Response({"error": "Quantity not set"},status=status.HTTP_400_BAD_REQUEST)

    try:
        item = CartItem.objects.get(id=id)
    except CartItem.DoesNotExist:
        return Response({"error": "CartItem not found"}, status=status.HTTP_404_NOT_FOUND)
    item.quantity = quantity
    item.save()
    serializer = CartItemSerializer(item)
    return Response(data=serializer.data, status=status.HTTP_200_OK)