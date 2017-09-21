from escpos.printer import Usb


class Address:

    def __init__(self, id_vendor, id_product):
        self.id_vendor = id_vendor
        self.id_product = id_product


class Printer:

    def __init__(self, address):
        self.printer = Usb(address.id_vendor, address.id_product)

    def print(self, message):
        self.printer.text(message)
        self.printer.cut()
