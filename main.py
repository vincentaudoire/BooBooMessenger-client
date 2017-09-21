from service.messageService import MessageService
from network.networkLayer import NetworkLayer
from printer.printer import Printer, Address
from time import sleep


class BooBooMessenger:

    FETCHING_TIME = 120  # Fetch an print messages every x seconds
    PRINTER_VENDOR = 0x0416
    PRINTER_PRODUCT = 0x5011

    def __init__(self):
        self.printer = Printer(Address(id_vendor=self.PRINTER_VENDOR, id_product=self.PRINTER_PRODUCT))
        self.network_layer = NetworkLayer(endpoint="https://booboomessenger.herokuapp.com/")
        self.service = MessageService(network_layer=self.network_layer)

    def run(self):
        while True:
            self.fetch_and_print_messages()
            sleep(self.FETCHING_TIME)

    def fetch_and_print_messages(self):

        print("-- Fetching messages --")

        all_messages = self.service.get_messages()

        if len(all_messages) == 0:
            print("No new messages")

        for message_to_be_printed in all_messages:
            self.printer.print(message_to_be_printed.message)
            self.service.mark_message_as_printed(message_to_be_printed)


if __name__ == "__main__":
    app = BooBooMessenger()
    app.run()
