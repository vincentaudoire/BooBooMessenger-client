from service.messageService import MessageService
from network.networkLayer import NetworkLayer
from printer.printer import Printer

if __name__ == "__main__":

    printer = Printer(address="123")
    network_layer = NetworkLayer(endpoint="https://booboomessenger.herokuapp.com/")
    service = MessageService(network_layer=network_layer)

    all_messages = service.get_messages()

    for message_to_be_printed in all_messages:
        printer.print(message_to_be_printed.message)
        service.mark_message_as_printed(message_to_be_printed)
