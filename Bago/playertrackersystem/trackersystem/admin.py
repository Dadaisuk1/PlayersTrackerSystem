from django.contrib import admin
from game.models import Game
from hero.models import Hero

# Register your models here.
admin.site.register(Hero)
admin.site.register(Game)
