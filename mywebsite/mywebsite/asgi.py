"""
ASGI config for mywebsite project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""


import os

from django.core.asgi import get_asgi_application # supports WSGI protocol by default
from channels.routing import ProtocolTypeRouter, URLRouter
# supports HTTP and Websocket protocols / routing
from channels.auth import AuthMiddlewareStack # supports Django's authentication system
import chat.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mywebsite.settings')

# application = get_asgi_application()

application = ProtocolTypeRouter({
	'http': get_asgi_application(),	# Just HTTP for now. (We can add other protocols later.)

	'websocket': AuthMiddlewareStack( # This is a middleware that will allow us to use Django's authentication system
		URLRouter( # URLRouter is a class that routes
			chat.routing.websocket_urlpatterns
		)
	)
})
