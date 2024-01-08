from django.shortcuts import render, get_object_or_404
from .models import Item
from django.views.generic import DetailView


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/detail.html'
    context_object_name = 'item'


def item_list(request):
    items = Item.objects.all()
    return render(request, 'item_list.html', {'items': items})
