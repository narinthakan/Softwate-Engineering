from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, ShoppingItemForm
from .models import ShoppingItem

def home_page(request):
    return render(request, 'home.html')

@login_required
def dashboard(request):
    items = ShoppingItem.objects.filter(owner=request.user)
    return render(request, 'dashboard.html', {'items': items})

def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, "ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง")
    return render(request, "login.html")

def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = SignUpForm()
    return render(request, 'sign_up.html', {'form': form})

@login_required
def add_item(request):
    if request.method == 'POST':
        form = ShoppingItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.owner = request.user
            item.save()
            return redirect('dashboard')
    else:
        form = ShoppingItemForm()
    return render(request, 'add_item.html', {'form': form})

@login_required
def edit_item(request, pk):
    item = ShoppingItem.objects.get(pk=pk)
    if request.method == 'POST':
        form = ShoppingItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ShoppingItemForm(instance=item)
    return render(request, 'edit_item.html', {'form': form})

@login_required
def delete_item(request, pk):
    item = ShoppingItem.objects.get(pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard')
    return render(request, 'delete_item.html', {'item': item})


def view_items(request):
    return render(request, 'view_items.html') 

def group_items(request):
    return render(request, 'group_items.html')  # สร้างไฟล์ group_items.html ด้วย