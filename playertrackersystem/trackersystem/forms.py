# heroes/forms.py
from django import forms
from .models import Hero
from .models import Game

class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero
        fields = ['hero_name', 'role']

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['game_name', 'game_type', 'image']
