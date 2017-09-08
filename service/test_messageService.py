from unittest import TestCase
from network.networkLayer import AbstractNetworkLayer
from service.messageService import MessageService


class MockNetworkLayer(AbstractNetworkLayer):

    def __init__(self):
        self.hasMarkedMessageAsPrinted = False

    def get(self, path):
        return [
            {
                "id": "123",
                "message": "Hello world",
                "received": "123"
            }
        ]

    def put(self, path):
        self.hasMarkedMessageAsPrinted = True


class TestMessageService(TestCase):

    def test_get_messages(self):
        service = MessageService(network_layer=MockNetworkLayer())
        messages = service.get_messages()

        self.assertEqual(len(messages), 1)

    def test_mark_message_as_printed(self):
        network_layer = MockNetworkLayer()
        service = MessageService(network_layer=network_layer)
        messages = service.get_messages()
        service.mark_message_as_printed(message=messages[0])

        self.assertTrue(network_layer.hasMarkedMessageAsPrinted)
