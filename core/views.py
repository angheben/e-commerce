from django.views.generic import ListView, TemplateView, FormView
from item.models import Category, Item
from .forms import SingupForm


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


class FormsView(FormView):
    template_name = 'core/signup.html'
    form_class = SingupForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.form_class()
        return context


