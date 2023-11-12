from asgiref.sync import async_to_sync
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.generic.websocket import WebsocketConsumer
import json


class MySyncConsumer(SyncConsumer):
    def connet(self, event):
        print("Websocket connected....")

    def receive(self, event):
        print("Message received....")

    def disconnect(self, event):
        print("Websocket disconnected...")


class MyAsyncConsumer(AsyncConsumer):
    async def connet(self, event):
        print("Websocket connected....")
        await self.accept()

    async def receive(self, text_data):
        print("Message received....")
        await self.send(text_data=json.dumps({
            'message': text_data
        }))

    async def disconnect(self, event):
        print("Websocket disconnected...")


class TestConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = "Test Room"
        self.room_group_name = "Test Room Group Name"
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,  # Use the updated group name here
            self.channel_name
        )
        self.accept()
        self.send(text_data=json.dumps({"status": "connected"}))

    def receive(self, text_data=None, bytes_data=None):
        pass

    def disconnect(self, code):
        pass
