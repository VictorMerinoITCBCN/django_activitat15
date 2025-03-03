from django.db import models
from django.db.models import CASCADE
from user.models import User
from catalog.models import Product


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=CASCADE)
    created_at = models.DateTimeField(auto_now=True)

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=CASCADE)
    product = models.ForeignKey(Product, on_delete=CASCADE)
    quantity = models.PositiveIntegerField()