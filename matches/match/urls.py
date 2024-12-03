from django.urls import path
from . import views

urlpatterns = [
    path('', views.match_list, name='match_list'),
    path('<int:pk>/', views.match_detail, name='match_detail'),
    path('create/', views.match_create, name='match_create'),
    path('<int:pk>/edit/', views.match_update, name='match_update'),
    path('<int:pk>/delete/', views.match_delete, name='match_delete'),
]
