from django.urls import path
# from django.contrib.auth.views import LoginView
from .views import home_page, dashboard, login_view, sign_up, add_item, edit_item, delete_item
from . import views

urlpatterns = [
    path('', home_page, name='home'),
    path('dashboard/', dashboard, name='dashboard'),
    path('login/', login_view, name='login'),
    path('sign-up/', sign_up, name='sign_up'),
    path('add-item/', add_item, name='add_item'),
    path('edit-item/<int:pk>/', edit_item, name='edit_item'),
    path('delete-item/<int:pk>/', delete_item, name='delete_item'),
    path('view-items/', views.view_items, name='view_items'),
    path('group-items/', views.group_items, name='group_items'),  # เพิ่มเส้นทางนี้
    
    
    
]
