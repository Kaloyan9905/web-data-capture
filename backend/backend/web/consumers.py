import json

from asgiref.sync import sync_to_async
from channels.generic.websocket import AsyncWebsocketConsumer

from backend.web.models import Data
from backend.web.webcam import capture_image


class DataConsumer(AsyncWebsocketConsumer):
    async def connect(self) -> json:
        await self.accept()
        text_data = json.dumps({'message': 'Connection established!'})
        await self.send(text_data)

    async def disconnect(self, close_code):
        pass

    async def receive(self, text_data) -> json:
        data_json = json.loads(text_data)

        clicked_x = data_json['clicked_x']
        clicked_y = data_json['clicked_y']
        image_url = await capture_image()

        await sync_to_async(Data.objects.create)(
            coordinate_x=clicked_x,
            coordinate_y=clicked_y,
            image=image_url,
        )

        await self.send(text_data=json.dumps({'image_url': image_url}))
