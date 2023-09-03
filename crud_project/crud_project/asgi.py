import os
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path
from .consumers import CrudConsumer

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crud_project.settings')

application = ProtocolTypeRouter(
    {
        'http': get_asgi_application(),
        'websocket': URLRouter([
            path('ws/crud/', CrudConsumer.as_asgi()),
        ]),
    }
)