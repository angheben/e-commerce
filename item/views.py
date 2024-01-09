from django.shortcuts import render, get_object_or_404
from .models import Item
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/detail.html'
    context_object_name = 'item'


def item_list(request, pk):
    item = get_object_or_404(Item, pk=pk)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=pk)[0:3]
    return render(request, 'item/detail.html', {
        'item': item,
        'related_items': related_items,
    })
