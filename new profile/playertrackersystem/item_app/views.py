# item_app/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Item
from .forms import ItemForm

def item_list(request):
    items = Item.objects.all()  # This should return all items
    return render(request, 'item_app/item_list.html', {'items': items})


def item_create(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('item_list')
    else:
        form = ItemForm()
    return render(request, 'item_app/item_form.html', {'form': form})

def item_detail(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'item_app/item_detail.html', {'item': item})

def item_update(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('item_detail', pk=item.pk)
    else:
        form = ItemForm(instance=item)
    return render(request, 'item_app/item_form.html', {'form': form})

def item_delete(request, pk):
    item = get_object_or_404(Item, pk=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('item_list')
    return render(request, 'item_app/item_confirm_delete.html', {'item': item})
