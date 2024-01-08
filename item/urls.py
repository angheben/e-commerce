from django.urls import path
from .views import ItemDetailView, item_list
from django.conf import settings
from django.conf.urls.static import static

app_name = 'item'

urlpatterns = [
    path('<int:pk>/', ItemDetailView.as_view(), name='detail'),  # Detail view URL pattern
    path('list/', item_list, name='list'),  # URL pattern for item list view if needed
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

