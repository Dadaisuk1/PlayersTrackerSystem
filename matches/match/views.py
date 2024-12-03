from django.shortcuts import render, get_object_or_404, redirect
from .models import Match
from .forms import MatchForm

# List all matches
def match_list(request):
    matches = Match.objects.all()
    return render(request, 'match/match_list.html', {'matches': matches})

# View match details
def match_detail(request, pk):
    match = get_object_or_404(Match, pk=pk)
    return render(request, 'match/match_detail.html', {'match': match})

# Create a new match
def match_create(request):
    if request.method == 'POST':
        form = MatchForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('match_list')
    else:
        form = MatchForm()
    return render(request, 'match/match_form.html', {'form': form})

# Update an existing match
def match_update(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        form = MatchForm(request.POST, instance=match)
        if form.is_valid():
            form.save()
            return redirect('match_list')
    else:
        form = MatchForm(instance=match)
    return render(request, 'match/match_form.html', {'form': form})

# Delete a match
def match_delete(request, pk):
    match = get_object_or_404(Match, pk=pk)
    if request.method == 'POST':
        match.delete()
        return redirect('match_list')
    return render(request, 'match/match_confirm_delete.html', {'match': match})
