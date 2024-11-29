from django.shortcuts import render, redirect, get_object_or_404
from .models import Hero
from .forms import HeroForm
from accounts.models import Player

# Create your views here.
# READ - List all heroes
def hero_list(request):
    heroes = Hero.objects.all()
    player_id = request.session.get('player_id')  # Retrieve player ID from session
    player = Player.objects.get(playerID=player_id) if player_id else None  # Fetch Player object or set to None
    return render(request, 'hero_list.html', {'heroes': heroes, 'player'  : player})
    

# CREATE - Add a new hero
def hero_create(request):
    player_id = request.session.get('player_id')  # Retrieve player ID from session
    player = Player.objects.get(playerID=player_id) if player_id else None  # Fetch Player object or set to None
    if request.method == 'POST':
        form = HeroForm(request.POST, request.FILES)  # Add request.FILES to handle file upload
        if form.is_valid():
            # Save the form and then redirect to hero list
            form.save()
            return redirect('hero_list')
            
    else:
        form = HeroForm()
    
    return render(request, 'hero_form.html', {'form': form, 'player' : player})

# UPDATE - Edit an existing hero
def hero_update(request, id):
    hero = get_object_or_404(Hero, hero_id=id)
    if request.method == 'POST':
        form = HeroForm(request.POST, instance=hero)
        if form.is_valid():
            form.save()
            return redirect('hero_list')
    else:
        form = HeroForm(instance=hero)
    return render(request, 'hero_form.html', {'form': form})

# DELETE - Remove a hero
def hero_delete(request, id):
    hero = get_object_or_404(Hero, hero_id=id)
    if request.method == 'POST':
        hero.delete()
        return redirect('hero_list')
    return render(request, 'hero_confirm_delete.html', {'hero': hero})