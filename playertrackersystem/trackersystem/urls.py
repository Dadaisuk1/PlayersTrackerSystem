# urls.py
from . import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.landing_page, name='landing_page'),  # Landing page as the root URL
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    path('heroes/', include('hero.urls')),
    # Game URLs
    path('game/<str:game_name>/', views.game_detail, name='game_detail'),
    path('game/create/', views.game_create, name='game_create'),
    path('game/update/<int:game_id>/', views.game_update, name='game_update'),
    path('game/delete/<int:game_id>/', views.game_delete, name='game_delete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)