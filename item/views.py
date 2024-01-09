from django.views.generic import DetailView
from .models import Item


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item/detail.html'
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item = self.get_object()  # Retrieve the current item

        # Get related items
        related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(pk=item.pk)[:3]

        # Add related items to the context
        context['related_items'] = related_items
        return context
