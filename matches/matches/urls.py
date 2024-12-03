from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('matches/', include('match.urls')),  # This connects the match app's URLs
]
