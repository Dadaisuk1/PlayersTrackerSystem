from django.urls import path
from trackersystem import views
from . import views  # Import your views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Default route to login page
    # path('', views.home_page, name='home'),
    path('home/', views.home_page, name='home'),
    path('logout/', views.logout_view, name='logout'),  # Logout route
    path('login/', views.login_view, name='login'),
    path('register/', views.register_player, name='register'),  # Registration page
    path('players/', views.player_list, name='player_list'),  # List all players
    path('update/<int:playerID>/', views.update_player, name='update_player'),  # Update player details
    path('delete/<int:playerID>/', views.delete_player, name='delete_player'),  # Delete a player
    path('profile/edit/', views.edit_profile_view, name='edit_profile'), 
    path('profile/', views.profile_view, name='profile'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

