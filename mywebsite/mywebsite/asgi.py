"""
ASGI config for mywebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""


import os

# To route WebSocket requests to the appropriate consumer

from django.core.asgi import get_asgi_application  # ASGI application handler for Django, which also supports WSGI by default
from channels.routing import ProtocolTypeRouter, URLRouter  # Handles protocol-based routing (e.g., HTTP, WebSocket)
from channels.auth import AuthMiddlewareStack  # Middleware to enable Django's authentication system for WebSocket connections
import chat.routing  # Importing the chat app's routing configuration

# Set the default settings module for the Django project
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

# Define the main ASGI application instance
application = ProtocolTypeRouter({
    # Route HTTP requests using Django's ASGI application
    'http': get_asgi_application(),

    # Route WebSocket connections with authentication support
    'websocket': AuthMiddlewareStack(
        # URLRouter maps WebSocket connections to the specified URL patterns
        URLRouter(
            chat.routing.websocket_urlpatterns  # Use the WebSocket URL patterns defined in the chat app's routing
        )
    )
})

# QUESTION: can it be done in routing.py? 
# we are referring here to chat/routing.py