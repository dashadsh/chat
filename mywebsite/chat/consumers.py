# Consumer is a class that has methods that handle Websocket events
# It is similar to a Django view, but it handles Websocket events instead of HTTP requests

import json
from channels.generic.websocket import WebsocketConsumer # this is a class that we inherit from
from asgiref.sync import async_to_sync

class ChatConsumer(WebsocketConsumer):
	def connect(self): # This method is called when the websocket is handshaking as part of the connection process
		self.room_group_name = 'test'

		async_to_sync(self.channel_layer.group_add)(
			self.room_group_name,
			self.channel_name
		)

		self.accept()

		# self.send(text_data=json.dumps({
		# 	'type': 'connection established',
		# 	'message' : 'You are now connected'
		# }))


# ------------------------------------------------------------------------------

	# def disconnect(self, close_code):
	# 	pass


# ------------------------------------------------------------------------------


	def receive(self, text_data):
		text_data_json = json.loads(text_data) # parse the JSON data that the client sent to the server
		message = text_data_json['message'] # This is the message that the client sent to the server

		# print('Message:', message)

		# self.send(text_data=json.dumps({
		# 	'type': 'chat', # This is the type of message that the server is sending to the client
		# 	'message': message,
		# }))

		async_to_sync(self.channel_layer.group_send)(
			self.room_group_name,
			{
				'type': 'chat_message',
				'message': message
			}
		)

# ------------------------------------------------------------------------------

	def chat_message(self, event):
		message = event['message']

		self.send(text_data=json.dumps({
			'type': 'chat',
			'message': message,
		}))