# heroes/forms.py
from django import forms
from game.models import Game

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['game_name', 'game_type', 'image']
