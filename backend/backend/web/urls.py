from django.urls import path

from backend.web.views import index

urlpatterns = (
    path('', index),
)
