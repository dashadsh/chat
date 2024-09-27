daphne -p 8000 mywebsite.asgi:application \
uvicorn mywebsite.asgi:application --host 127.0.0.1 --port 8000


if daphne added to installed apps:\
python3 manage.py runserver

# WebSocket Communication Flow: Frontend and Backend Interaction

This document explains the step-by-step flow of how the backend and frontend communicate using WebSockets in a simple chat application.

## **Step 1: User Sends a Message (Frontend → Backend)**

1. **User types a message in the input box** and clicks the "Send" button in the HTML form.

2. **The form submission triggers a JavaScript event:**
   - The `form.addEventListener('submit', ...)` function captures this event.
   - `e.preventDefault()` prevents the page from refreshing when the form is submitted.
   
3. **Sending the message to the WebSocket:**
   - `let message = e.target.message.value;` captures the input message.
   - `chatSocket.send(JSON.stringify({'message': message}));` sends the message as a JSON object to the WebSocket server.

## **Step 2: Backend Receives and Processes the Message (Backend)**

4. **The `receive` method in the `ChatConsumer` class gets called:**
   - This method is triggered when the backend receives a message from the WebSocket client (the browser).
   - `text_data_json = json.loads(text_data)`: Parses the JSON data received from the frontend.
   - `message = text_data_json['message']`: Extracts the actual message text sent by the user.

5. **Broadcast the message to all connected clients in the chat room:**
   - `async_to_sync(self.channel_layer.group_send)(...)` sends the message to all clients connected to the group (including the sender).
   - This triggers the `chat_message` method defined in the same `ChatConsumer` class.

## **Step 3: Backend Sends the Message to All Clients (Backend → Frontend)**

6. **The `chat_message` method is called:**
   - This method is invoked by the `group_send` function with the event type `chat_message`.
   - It extracts `message = event['message']` from the received event.

7. **Sending the message back to all connected WebSocket clients:**
   - `self.send(text_data=json.dumps({'type': 'chat', 'message': message}))`: This sends the message back to all clients as a JSON object.

## **Step 4: All Clients Receive the Message (Frontend)**

8. **The `onmessage` event listener in JavaScript gets triggered:**
   - `chatSocket.onmessage = function(e) {...}` executes when the message is received from the WebSocket server.
   - `let data = JSON.parse(e.data);` parses the received JSON data.

9. **Display the received message:**
   - The message is inserted into the HTML `#messages` container with different styles:
     - If the message was sent from the current tab, it displays in green (`sent-message` class).
     - If received from another tab/user, it displays in red (`received-message` class).

## **Summary Flow**

1. **Frontend:** User submits a message → `chatSocket.send()` sends the message via WebSocket.
2. **Backend:** `ChatConsumer.receive()` processes the message → broadcasts to all group members using `group_send`.
3. **Backend:** `ChatConsumer.chat_message()` sends the message back to all WebSocket clients.
4. **Frontend:** `chatSocket.onmessage` handles the received message and updates the chat display.

## **Key Points of Communication**

- **WebSocket connection (`chatSocket`)**: Establishes real-time communication between frontend (HTML/JavaScript) and backend (`ChatConsumer`).
- **`receive` method**: Handles incoming messages from the frontend.
- **`group_send` and `chat_message`**: Manages broadcasting messages to all clients in real-time.
- **HTML/JavaScript**: Displays the message in the chat interface on each client's browser.



