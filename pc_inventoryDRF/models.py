from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Brand(models.Model):
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Component(models.Model):
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    name = models.CharField(max_length=255)
    date_creation = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name