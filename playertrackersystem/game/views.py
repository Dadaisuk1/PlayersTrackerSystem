from django.shortcuts import render, redirect, get_object_or_404
from .models import Game
from .forms import GameForm

# CREATE - Add a new game
def game_create(request):
    if request.method == 'POST':
        form = GameForm(request.POST, request.FILES)  # Handle file uploads
        if form.is_valid():
            form.save()
            return redirect('game_list')  # Redirect to the game list page
    else:
        form = GameForm()
    return render(request, 'game_create.html', {'form': form})


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

