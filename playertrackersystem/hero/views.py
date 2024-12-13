from django.shortcuts import render, redirect, get_object_or_404
from .models import Hero
from .forms import HeroForm
from accounts.models import Player

# Create your views here.
# READ - List all heroes
def hero_list(request):
    heroes = Hero.objects.all()
    return render(request, 'hero_list.html', {'heroes': heroes})
    

# CREATE - Add a new hero
def hero_create(request):
    if request.method == 'POST':
        form = HeroForm(request.POST, request.FILES)  # Add request.FILES to handle file upload
        print(request.POST)
        if form.is_valid():
            # Save the form and then redirect to hero list
            form.save()
            return redirect('hero_list')
            
    else:
        form = HeroForm()
    
    return render(request, 'hero_form.html', {'form': form})

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