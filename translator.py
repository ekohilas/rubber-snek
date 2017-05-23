import pyb
from keys import KEYS, KEYS_SHIFT, MODS
KEYBOARD = pyb.USB_HID()
KEY_UP = bytearray(8)

def map_char(char):
    array = bytearray(8)

    if char in KEYS_SHIFT:
        array[0] = MODS["LSHIFT"]
        array[2] = KEYS_SHIFT[char]
    else:
        array[2] = KEYS[char]

    return array

def send_char(char):
    KEYBOARD.send(map_char(char))
    pyb.delay(8)
    KEYBOARD.send(KEY_UP)
    pyb.delay(8)

def send_string(string):

    char, string = string[0], string[1:]
    while char:

        if char == "\\":

            escape = ""
            char, string = string[0], string[1:]
            while char != "\\":
                escape += char
                char, string = string[0], string[1:]

            if escape:
                send_char(escape)
            else:
                send_char("\\")
        else:
            send_char(char)

        if string:
            char, string = string[0], string[1:]
        else:
            char = ""

if __name__ == "__main__":
    while True:
        if pyb.Switch()():
            send_string("hello world")
