from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ShoppingItem(models.Model):
    STATUS_CHOICES = [
        ('pending', 'ยังไม่ซื้อ'),
        ('purchased', 'ซื้อแล้ว'),
    ]

    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    reminder = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name