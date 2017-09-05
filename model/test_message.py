from unittest import TestCase
from model.message import Message
from model.error import MissingKeyError

class TestMessage(TestCase):

    def test_should_deserialize(self):

        id = "123"
        message = "Hello world"
        received = "2017-09-03T22:02:04.706165Z"

        dictionary = {'id': id, 'message': message, 'received': received}

        deserialized_message = Message(dictionary)

        self.assertEqual(deserialized_message.id, id)
        self.assertEqual(deserialized_message.message, message)
        self.assertTrue(deserialized_message.received, received)

    def test_should_raise_missing_data_exception(self):
        id = "123"

        dictionary = {'id': id}

        with self.assertRaises(MissingKeyError):
            Message(dictionary)
