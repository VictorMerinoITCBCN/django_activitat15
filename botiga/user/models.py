from django.db import models

class User(models.Model):
    name = models.CharField(null=False,max_length=50)
    last_name = models.CharField(null=False, max_length=100)
    email = models.EmailField(null=False, unique=True)
    password = models.CharField(null=False)