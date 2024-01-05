from django.views.generic import ListView, TemplateView
from item.models import Category, Item


class IndexView(ListView):
    template_name = 'index.html'
    context_object_name = 'items'
    queryset = Item.objects.filter(is_sold=False)[:6]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class ContactView(TemplateView):
    template_name = 'core/contact.html'
