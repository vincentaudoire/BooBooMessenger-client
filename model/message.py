from model.error import MissingKeyError


class Message:
    def __init__(self, id, message, received):
        self.id = id
        self.message = message
        self.received = received

    def __init__(self, dictionary):
        try:
            self.id = dictionary['id']
            self.message = dictionary['message']
            self.received = dictionary['received']
        except KeyError:
            raise MissingKeyError
