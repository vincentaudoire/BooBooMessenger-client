from model.message import Message


class MessageService:

    def __init__(self, network_layer):
        self.network_layer = network_layer

    def get_messages(self):
        raw_messages = self.network_layer.get("/messages")
        messages = list(map(lambda m: Message(dictionary=m), raw_messages))
        return messages

    def mark_message_as_printed(self, message):
        path = "/messages/" + message.id + "/printed"
        self.network_layer.put(path)

