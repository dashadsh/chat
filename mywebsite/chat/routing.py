# routing.py is the Channels routing configuration file. 
# It tells Channels what code to run when an HTTP request is received by the server. 
# In this case, it tells Channels to run the Django application when an HTTP request is received. 
# This is necessary because Channels uses a different protocol (ASGI) than Django's built-in development server (WSGI).


from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
	re_path(r'ws/socket-server/$', consumers.ChatConsumer.as_asgi())
]