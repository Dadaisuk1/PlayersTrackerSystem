from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Game URLs
    path('game/create/', views.game_create, name='game_create'),
    path('game/<str:game_name>/', views.game_detail, name='game_detail'),
    path('game/update/<int:game_id>/', views.game_update, name='game_update'),
    path('game/delete/<int:game_id>/', views.game_delete, name='game_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)