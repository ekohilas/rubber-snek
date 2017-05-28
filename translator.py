import pyb
from keys import KEYS, KEYS_SHIFT, MODS
KEYBOARD = pyb.USB_HID()
KEY_UP = bytearray(8)
LINUX_TERMINAL = bytearray(8)
LINUX_TERMINAL[0], LINUX_TERMINAL[2] = MODS["LCTRL"] + MODS["LALT"], KEYS["t"]
CHANGE_WINDOW = bytearray(8)
CHANGE_WINDOW[0], CHANGE_WINDOW[2] = MODS["LALT"], KEYS["TAB"]

def windows_terminal():
    run = bytearray(8)
    run[0], run[2] = MODS["LMETA"], KEYS["r"]
    send_array(run)
    pyb.delay(100)
    send_string("cmd\\ENTER\\")
    pyb.delay(100)

def map_char(char):
    array = bytearray(8)

    if char in KEYS_SHIFT:
        array[0] = MODS["LSHIFT"]
        array[2] = KEYS_SHIFT[char]
    else:
        array[2] = KEYS[char]

    return array

def send_array(array):
    KEYBOARD.send(array)
    pyb.delay(8)
    KEYBOARD.send(KEY_UP)
    pyb.delay(8)

def send_char(char):
    send_array(map_char(char))

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
            if os_name == "nt":

            else:
                send_array(LINUX_TERMINAL)
                #send_array(CHANGE_WINDOW)
                pyb.delay(500)
                send_string("echo 'hello world!'\\ENTER\\")

