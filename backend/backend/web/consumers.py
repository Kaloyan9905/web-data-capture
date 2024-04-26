import json
from channels.generic.websocket import AsyncWebsocketConsumer


class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        text_data = json.dumps({'message': 'Connection established!'})
        await self.send(text_data)

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data):
        data_json = json.loads(text_data)
        clicked_x = data_json['clicked_x']
        clicked_y = data_json['clicked_y']
        print(clicked_x)
        print(clicked_y)
        # TODO: save the data into a model with web cam image!
        await self.send(text_data=json.dumps({'message': 'received coordinates'}))
