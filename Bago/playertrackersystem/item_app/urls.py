# item_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),  # List view for items
    path('new/', views.item_create, name='item_create'),  # Create new item (corrected name)
    path('<int:pk>/', views.item_detail, name='item_detail'),  # Detail view for a specific item
    path('update/<int:pk>/', views.item_update, name='item_update'),  # Update an existing item
    path('delete/<int:pk>/', views.item_delete, name='item_delete'),  # Delete an existing item
]
