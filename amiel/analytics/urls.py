from django.urls import path
from . import views

urlpatterns = [
    path('', views.analytics_list, name='analytics_list'),  # List all entries
    path('create/', views.analytics_create, name='analytics_create'),  # Create new entry
    path('<int:pk>/update/', views.analytics_update, name='analytics_update'),  # Update existing entry
    path('<int:pk>/delete/', views.analytics_delete, name='analytics_delete'),  # Delete entry
]
