from django.urls import re_path

from backend.web import consumers

websocket_urlpatterns = [
    re_path('ws/socket-server/', consumers.DataConsumer.as_asgi()),
]
