from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.hashers import check_password
# from django.http import HttpResponse

from .models import Player, Game, Hero, Match
# from django.contrib.auth.models import User

# imported from Forms
from .forms import PlayerForm, GameForm

# imported outside
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def landing (request):
    return render (request, 'pages/landing.html');

def home(request):
    games = Game.objects.all()  # Fetch all games
    return render(request, 'pages/home.html', {'games': games})

def game_detail(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    heroes = game.heroes.all()  # Get all heroes for this game
    matches = game.matches.all()  # Get all matches for this game
    return render(request, 'pages/game.html', {'game': game, 'heroes': heroes, 'matches': matches})

# View to create a game
def create_game(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        game = Game.objects.create(name=name, description=description)
        return redirect('game_detail', game_id=game.id)  # Redirect to the game detail page
    return render(request, 'pages/admin/game.html')

# Directory when i click a game
def game_detail(request, game_name):
    # Fetch the game based on the name
    game = Game.objects.get(game_name = game_name)
    return render(request, 'pages/user/game_detail.html', {'game': game})

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


















# View to create a hero
def create_hero(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        name = request.POST.get('name')
        level = int(request.POST.get('level'))
        hero = Hero.objects.create(game=game, name=name, level=level)
        return redirect('game_detail', game_id=game.id)  # Redirect to game detail
    return render(request, 'pages/admin/hero.html', {'game': game})

# View to create a match
def create_match(request, game_id):
    game = get_object_or_404(Game, id=game_id)
    if request.method == 'POST':
        hero_1_id = int(request.POST.get('hero_1'))
        hero_2_id = int(request.POST.get('hero_2'))
        hero_1 = get_object_or_404(Hero, id=hero_1_id)
        hero_2 = get_object_or_404(Hero, id=hero_2_id)
        match = Match.objects.create(game=game, hero_1=hero_1, hero_2=hero_2)
        return redirect('game_detail', game_id=game.id)  # Redirect to game detail
    heroes = game.heroes.all()
    return render(request, 'pages/admin/match.html', {'game': game, 'heroes': heroes})

# Signup view
def sign_up(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = PlayerForm()
    return render(request, 'pages/signup.html', {'form': form})

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            player = Player.objects.get(username=username)
            if check_password(password, player.password):  # Verify the password
                request.session['player_id'] = player.playerID  # Store player ID in session
                return redirect('home')  # Redirect to home page
            else:
                messages.error(request, 'Invalid username or password')
        except Player.DoesNotExist:
            messages.error(request, 'Invalid username or password')

    return render(request, 'pages/login.html')

# Logout view
def logout_view(request):
    request.session.flush()  # Clear the entire session
    return redirect('login')  # Red

# Home view (protected by login_required)
def home(request):
    player_id = request.session.get('player_id')
    if player_id:
        player = Player.objects.get(playerID=player_id)
        return render(request, 'pages/home.html', {'player': player})
    return redirect('login')


# View all players (protected by login_required)

def player_list(request):
    players = Player.objects.all()  # Get all players
    return render(request, 'pages/player_list.html', {'players': players})


# Update an existing player

def update_player(request, playerID):
    player = get_object_or_404(Player, playerID=playerID)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'pages/user/update.html', {'form': form})


# Delete a player

def delete_player(request, playerID):
    player = get_object_or_404(Player, playerID=playerID)
    if request.method == 'POST':
        player.delete()  # Delete the player
        return redirect('player_list')
    return render(request, 'delete_player.html', {'player': player})

def profile_view(request):
    player_id = request.session.get('player_id')
    if player_id:
        player = Player.objects.get(playerID=player_id)  # Get the player instance

        # Display profile (view-only mode)
        return render(request, 'pages/user/profile.html', {'player': player})  # Pass the player instance to template
    
    return redirect('login')  # If player not found in session, redirect to login

def edit_profile_view(request):
    player_id = request.session.get('player_id')
    if player_id:
        player = Player.objects.get(playerID=player_id)  # Get the player instance

        if request.method == 'POST':
            form = PlayerForm(request.POST, request.FILES, instance=player)  # Handle file upload
            if form.is_valid():
                form.save()
                messages.success(request, 'Profile updated successfully!')
                return redirect('profile')  # Redirect to the profile page after saving
        else:
            form = PlayerForm(instance=player)  # Pre-populate the form with player's data

        return render(request, 'pages/user/edit.html', {'form': form, 'player': player})  # Pass the form and player instance to template
    
    return redirect('plogin')  # If player not found in session, redirect to login





# Admin Dashboard
@login_required
def dashboard(request):
    # Get the logged-in user
    user = request.user

    # Get the corresponding player (if exists)
    player = Player.objects.filter(user=user).first()  # Get the player associated with the user

    # If you want to show all users and their players (optional)
    all_players = Player.objects.all()

    return render(request, 'pages/admin/dashboard.html', {
        'player': player,
        'all_players': all_players,  # Pass this to template if needed
    })