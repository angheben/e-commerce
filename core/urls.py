from django.urls import path
from .views import IndexView, ContactView, FormsView
from .forms import SingupForm

app_name = 'core'

urlpatterns = [
    path("", IndexView.as_view(), name='views'),
    path("contact/", ContactView.as_view(), name="contact"),
    path("signup/", FormsView.as_view(form_class=SingupForm), name='signup'),
]

"""if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"""

