from channels.generic.websocket import AsyncWebsocketConsumer
import json


class CrudConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Подключение клиента к WebSocket-каналу
        await self.accept()

    async def disconnect(self, close_code):
        # Отключение клиента от WebSocket-канала
        pass

    async def receive(self, text_data):
        # Обработка полученного сообщения от клиента
        data = json.loads(text_data)
        crud_object_id = data['crud_object_id']
        is_ready = data['is_ready']

        # Обновление значения поля "Ready" для объекта CrudModel
        crud_object = CrudModel.objects.get(id=crud_object_id)
        crud_object.ready = is_ready
        crud_object.save()

        # Отправка обратного сообщения всем подключенным клиентам
        await self.channel_layer.group_send(
            'crud_group',
            {
                'type': 'crud_update',
                'crud_object_id': crud_object_id,
                'is_ready': is_ready
            }
        )

    async def crud_update(self, event):
        # Обработка обратного сообщения и отправка его клиенту
        crud_object_id = event['crud_object_id']
        is_ready = event['is_ready']

        # Отправка обратного сообщения клиенту
        await self.send(text_data=json.dumps({
            'crud_object_id': crud_object_id,
            'is_ready': is_ready
        }))
