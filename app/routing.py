from django.urls import path
from . import consumers
websocket_urlpatterns = [
    path('ws/sc/', consumers.MySyncConsumer.as_asgi(), name='sync_consumers'),
    path('ws/ac/', consumers.MyAsyncConsumer.as_asgi(), name='async_consumers')
]