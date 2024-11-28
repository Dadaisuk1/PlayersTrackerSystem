from django import forms
from .models import Hero

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['hero_id', 'hero_name', 'role', 'match', 'image']