import pyb
from keys import KEYS, KEYS_SHIFT, MODS
KEYBOARD = pyb.USB_HID()
KEY_UP = bytearray(8)
TERMINAL = bytearray(8)
TERMINAL[0], TERMINAL[2] = MODS["LCTRL"] + MODS["LALT"], KEYS["t"]
CHANGE_WINDOW = bytearray(8)
CHANGE_WINDOW[0], CHANGE_WINDOW[2] = MODS["LALT"], KEYS["TAB"]

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

TOGGLE = False

def toggle():
    global TOGGLE
    TOGGLE = not TOGGLE

if __name__ == "__main__":
    accel = pyb.Accel()
    mouse = pyb.USB_HID()


    while True:
        pyb.Switch().callback(toggle)

        if TOGGLE:
            print("KEYBOARD")
            pyb.usb_mode('CDC+HID', hid=pyb.hid_keyboard)
            send_array(TERMINAL)
            #send_array(CHANGE_WINDOW)
            pyb.delay(500)
            send_string(r"echo 'hello world!'\ENTER\\")
            TOGGLE = False
        else:
            print("MOUSE")
            pyb.usb_mode('CDC+HID')
            mouse.send((0, accel.x(), -accel.y(), 0))
            pyb.delay(10)
        pyb.delay(100)
