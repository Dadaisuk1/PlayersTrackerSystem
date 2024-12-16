from django import forms
from .models import Player, Game
from django.contrib.auth.hashers import make_password

class PlayerForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        required=False,  # Allow the password field to be blank for updates
        help_text="Leave blank to keep the current password."
    )

    class Meta:
        model = Player
        fields = ['username', 'email', 'password', 'profile_picture']

    def save(self, commit=True):
        player = super().save(commit=False)
        # Only hash and update the password if it was provided
        if self.cleaned_data['password']:
            player.password = make_password(self.cleaned_data['password'])
        if commit:
            player.save()
        return player

class GameForm(forms.ModelForm):
    class Meta:
        model = Game
        fields = ['game_name', 'game_type', 'image']