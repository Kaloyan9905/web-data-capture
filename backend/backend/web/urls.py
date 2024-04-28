from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from backend.web.views import index

urlpatterns = [
    path('', index),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
