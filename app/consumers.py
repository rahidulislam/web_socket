from channels.consumer import SyncConsumer, AsyncConsumer


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

    async def receive(self, event):
        print("Message received....")

    async def disconnect(self, event):
        print("Websocket disconnected...")
