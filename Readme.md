[![Build Status](https://travis-ci.org/vincentaudoire/BooBooMessenger-client.svg?branch=master)](https://travis-ci.org/vincentaudoire/BooBooMessenger-client)

# BooBooMessenger-client

BooBooMessenger is a small project made to send and print messages using a ESC/POS receipt printer.

## Installation

### Requirement
- Python 3.5 
- [pip](https://pip.pypa.io/en/stable/installing/)

### Get the sources
```Bash
git clone https://github.com/vincentaudoire/BooBooMessenger-client.git
```

### Configuring the client
The current version is meant to work with the Zjiang ZJ-58 thermal printer. If you would like to use with another ESC/POS you will need to set `PRINTER_VENDOR` and `PRINTER_PRODUCT` with your printer values inside `main.py`

To find your printer vendor and product you can use `lsusb`.

### Install 3rd parties dependencies
```Bash
pip install -r requirements.txt
```

### Build and Run 
In `BooBooMessenger-client/` 
```Bash
python3.5 main.py
```

