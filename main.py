from service.messageService import MessageService
from network.network_layer import NetworkLayer


if __name__ == "__main__":

    network_layer = NetworkLayer(endpoint="https://booboomessenger.herokuapp.com/")
    service = MessageService(network_layer=network_layer)

    all_messages = service.get_messages()
    service.mark_message_as_printed(all_messages[0])
