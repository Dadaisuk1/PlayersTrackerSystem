from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('heroes/', views.hero_list, name='hero_list'),
    path('hero/create/', views.hero_create, name='hero_create'),
    path('hero/update/<int:id>/', views.hero_update, name='hero_update'),
    path('hero/delete/<int:id>/', views.hero_delete, name='hero_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
