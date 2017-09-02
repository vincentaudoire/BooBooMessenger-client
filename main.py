from escpos.printer import Usb

if __name__ == "__main__":
    printer = Usb(0x0416, 0x5011)
    printer.text("Hello world!")
