from django.urls import path, include
from app.consumers import ChatConsumer

websocket_urlpatterns = [
    path('',ChatConsumer.as_asgi())
]
