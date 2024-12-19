from django.contrib import admin
from .models import CustomUser, Category, ShoppingItem
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Category)
admin.site.register(ShoppingItem)