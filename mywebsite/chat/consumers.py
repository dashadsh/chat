import json
from channels.generic.websocket import WebsocketConsumer  # Base class for WebSocket consumers in Django Channels
from asgiref.sync import async_to_sync  # Utility to run async code in a synchronous context

class ChatConsumer(WebsocketConsumer):
    # This class manages WebSocket connections and events for a chat application.
    # It operates similarly to a Django view but is specifically designed to handle WebSocket events.

    def connect(self):
        # This method is called when the WebSocket connection is established.
        # It is part of the connection handshake process.

        self.room_group_name = 'test'  # Define the group name for the chat room

        # Add the current channel to the group, allowing it to receive messages sent to the group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name  # The unique name for the WebSocket connection
        )

        self.accept()  # Accept the WebSocket connection

        # Uncomment to send a confirmation message to the client upon connection establishment
        # self.send(text_data=json.dumps({
        #     'type': 'connection established',
        #     'message': 'You are now connected'
        # }))

    # ------------------------------------------------------------------------------

    # Uncomment this method to handle disconnection events
    # def disconnect(self, close_code):
    #     # This method is called when the WebSocket connection is closed
    #     pass

    # ------------------------------------------------------------------------------

    def receive(self, text_data):
        # This method is called when a message is received from the WebSocket client.
        
        text_data_json = json.loads(text_data)  # Parse the JSON data received from the client
        message = text_data_json['message']  # Set the message variable to the 'message' key in the JSON data

        # Uncomment to log the received message for debugging
        # print('Message:', message)

        # Send the received message to all members of the chat group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'chat_message',  # Define the type of event to be handled by chat_message method
                'message': message  # Pass the message to the group
            }
        )

    # ------------------------------------------------------------------------------

    def chat_message(self, event):
        # This method is called when a 'chat_message' event is received from the group.
        
        message = event['message']  # Extract the message from the event data

        # Send the message back to the WebSocket client
        self.send(text_data=json.dumps({
            'type': 'chat',  # Define the type of message being sent to the client
            'message': message,  # Include the actual message content
        }))
