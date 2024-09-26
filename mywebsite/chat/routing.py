from django.urls import re_path  # Import re_path to define URL patterns with regular expressions
from . import consumers  # Import the consumers module where WebSocket consumers are defined

# routing.py is the configuration file for Django Channels' routing.
# It specifies how to handle WebSocket connections and maps them to specific consumer classes.
# This is essential for enabling real-time features in your application, such as chat functionality.

# Define a list of URL patterns for WebSocket connections
websocket_urlpatterns = [
    # Use re_path to match the WebSocket URL and direct it to the ChatConsumer
    re_path(r'ws/socket-server/$', consumers.ChatConsumer.as_asgi())  # 
    # The URL pattern matches the WebSocket connection request at 'ws/socket-server/'
    # and routes it to the ChatConsumer, which handles the connection asynchronously.
]
