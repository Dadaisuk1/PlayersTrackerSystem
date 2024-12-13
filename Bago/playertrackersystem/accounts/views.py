from django.shortcuts import render, redirect, get_object_or_404
from .forms import PlayerForm
from .models import Player
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import check_password
from game.models import Game
from django.contrib.auth.hashers import make_password

# Home page view
def home_page(request):
    games = Game.objects.all()
    player_id = request.session.get('player_id')  # Get player ID from session
    if player_id:
        player = Player.objects.get(playerID=player_id)
        return render(request, 'home.html', {'games': games, 'player': player})
    return redirect('login')  # Redirect to login if no player is logged in

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
            messages.error(request, 'Player does not exist')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')  # Log unexpected errors

    return render(request, 'login.html')

# Logout view
def logout_view(request):
    request.session.flush()  # Clear the entire session
    return redirect('login')  # Red


# Home view (protected by login_required)

def home(request):
    player_id = request.session.get('player_id')
    if player_id:
        player = Player.objects.get(playerID=player_id)
        return render(request, 'home.html', {'player': player})
    return redirect('login')


# Register a new player
def register_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()  # Password will be hashed automatically
            return redirect('login')
    else:
        form = PlayerForm()
    return render(request, 'register.html', {'form': form})


# View all players (protected by login_required)

def player_list(request):
    players = Player.objects.all()  # Get all players
    return render(request, 'player_list.html', {'players': players})


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
    return render(request, 'update_player.html', {'form': form})


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
        return render(request, 'profile.html', {'player': player})  # Pass the player instance to template
    
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

        return render(request, 'edit_profile.html', {'form': form, 'player': player})  # Pass the form and player instance to template
    
    return redirect('login')  # If player not found in session, redirect to login