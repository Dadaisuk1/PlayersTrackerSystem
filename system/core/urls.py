from . import views
from django.urls import path
from .views import create_game
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Local Use
    # Default View
    path('', views.landing, name='landing-page'),

    # Home Views
    path('home/', views.home, name='home'),
    path('home/game/<int:game_id>', views.game_detail, name='game_detail'),

    # Account Views
    path('login/', views.login_view, name='login'), # Use Django's built-in login view
    path('signup/', views.sign_up, name='register'),
    path('logout/', views.logout_view, name='logout'),  # Use Django's built-in logout view

    # User
    path('user/', views.profile_view, name='profile'),
    path('user/update/<int:playerID>/', views.update_player, name='update_player'),  # Update player details
    path('user/delete/<int:playerID>/', views.delete_player, name='delete_player'),

    # Admin Side (for managing content)
    # path('manage/', views.dashboard, name='dashboard'),
    path('manage/user/', views.player_list, name='player_list'),

    path('manage/game/', create_game, name='create_game'),
    path('manage/game/<str:game_name>/', views.game_detail, name='game_detail'),
    path('manage/game/update/<int:game_id>/', views.game_update, name='game_update'),
    path('manage/game/delete/<int:game_id>/', views.game_delete, name='game_delete'),


    path('manage/hero/<int:game_id>/', views.create_hero, name='create_hero'),
    path('manage/match/<int:match_id>/', views.create_match, name='create_match')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
