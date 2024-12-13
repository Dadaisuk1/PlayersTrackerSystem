from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm
from accounts.models import Player

# Directory when i click a game
def game_detail(request, game_name):
    # Fetch the game based on the name
    game = Game.objects.get(game_name = game_name)
    player_id = request.session.get('player_id')  # Retrieve player ID from session
    player = Player.objects.get(playerID=player_id) if player_id else None  # Fetch Player object or set to None
    return render(request, 'game_detail.html', {'game': game, 'player': player})

# CREATE - Add a new game
def game_create(request):
    player_id = request.session.get('player_id')  # Retrieve player ID from session
    player = Player.objects.get(playerID=player_id) if player_id else None  # Fetch Player object or set to None
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('game_list.html')  # Redirect to the game list page
    else:
        form = GameForm()
    return render(request, 'game_create.html', {'form': form, 'player' : player})


# UPDATE - Edit an existing game
def game_update(request, game_id):  # Use game_id instead of id
    game = get_object_or_404(Game, game_id=game_id)  # Use game_id instead of id
    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameForm(instance=game)
    return render(request, 'game_form.html', {'form': form})

# DELETE - Remove a game
def game_delete(request, game_id):  # Use game_id instead of id
    game = get_object_or_404(Game, game_id=game_id)  # Use game_id instead of id
    if request.method == 'POST':
        game.delete()
        return redirect('game_list')
    return render(request, 'game_confirm_delete.html', {'game': game})

