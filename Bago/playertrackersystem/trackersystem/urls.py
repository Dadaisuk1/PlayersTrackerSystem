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
    path('game/', include('game.urls')),
    path('inventory/', include('item_app.urls')),
    
    
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)