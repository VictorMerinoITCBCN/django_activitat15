from django.db import models
from django.db.models import Model


# Create your models here.
class Product(models.Model):
    nom = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    preu = models.IntegerField()
    stock = models.IntegerField()
    categoria = models.CharField(max_length=200)
    img = models.CharField(max_length=200)

