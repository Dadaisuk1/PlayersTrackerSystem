from django.contrib import admin
from .models import Player, Game, Hero, Match
from django.utils.html import format_html

# Register your models here.
admin.site.register(Game)
admin.site.register(Hero)
admin.site.register(Match)

@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    search_fields = ('username', 'email')

    def profile_image_preview(self, obj):
        if obj.profile_image:
            return format_html('<img src="{}" width="50" height="50" style="border-radius: 50%;" />', obj.profile_image.url)
        return "No Image"
    
    profile_image_preview.short_description = "Profile Image"
