from django.shortcuts import render
from game.models import Game
from accounts.models import Player

# Create your views here.
def home_page(request):
    games = Game.objects.all()
    player_id = request.session.get('player_id')  # Retrieve player ID from session
    player = Player.objects.get(playerID=player_id) if player_id else None  # Fetch Player object or set to None
    return render(request, 'home.html', {'games': games, 'player': player})

def landing(request):
    return render (request, 'landing.html')
    