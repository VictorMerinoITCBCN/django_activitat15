from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    model = Product
    fields = '__all__'