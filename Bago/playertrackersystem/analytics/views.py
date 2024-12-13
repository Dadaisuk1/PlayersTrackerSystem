from django.shortcuts import render, get_object_or_404, redirect
from .models import Analytics
from .forms import AnalyticsForm

# List (Read) all Analytics entries
def analytics_list(request):
    analytics_entries = Analytics.objects.all()
    return render(request, 'analytics_list.html', {'analytics_entries': analytics_entries})

# Create a new Analytics entry
def analytics_create(request):
    if request.method == 'POST':
        form = AnalyticsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('analytics_list')  # Fixed the typo here
    else:
        form = AnalyticsForm()
    return render(request, 'analytics_form.html', {'form': form})

# Update an existing Analytics entry
def analytics_update(request, pk):
    analytics = get_object_or_404(Analytics, pk=pk)
    if request.method == 'POST':
        form = AnalyticsForm(request.POST, instance=analytics)
        if form.is_valid():
            form.save()
            return redirect('analytics_list')
    else:
        form = AnalyticsForm(instance=analytics)
    return render(request, 'analytics_form.html', {'form': form, 'analytics': analytics})

# Delete an Analytics entry
def analytics_delete(request, pk):
    analytics = get_object_or_404(Analytics, pk=pk)
    if request.method == 'POST':
        analytics.delete()
        return redirect('analytics_list')
    return render(request, 'analytics_confirm_delete.html', {'analytics': analytics})
