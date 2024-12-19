from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, ShoppingItem

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2']

class ShoppingItemForm(forms.ModelForm):
    class Meta:
        model = ShoppingItem
        fields = ['name', 'category', 'status', 'reminder']
