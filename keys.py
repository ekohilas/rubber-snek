#from pprint import pprint as print
letters         = {k: v for v, k in enumerate("abcdefghijklmnopqrstuvwxyz", start=4)}
letters_shift   = {k: v for v, k in enumerate("ABCDEFGHIJKLMNOPQRSTUVWXYZ", start=4)}
numbers         = {k: v for v, k in enumerate("1234567890", start=30)}
numbers_shift   = {k: v for v, k in enumerate("!@#$%^&*()", start=30)}
symbols_1       = {k: v for v, k in enumerate(" -=[]\\", start=44)}
symbols_1_shift = {k: v for v, k in enumerate(" _+{}|", start=44)}
symbols_2       = {k: v for v, k in enumerate(";'`,./", start=47)}
symbols_2_shift = {k: v for v, k in enumerate(':"~<>?', start=47)}

control = {
        "ENTER": 0x28,
        "ESC": 0x29,
        "BACKSPACE": 0x2a,
        "TAB": 0x2b,
        "CAPSLOCK": 0x39,
        "SYSRQ": 0x46,
        "SCROLLLOCK": 0x47,
        "PAUSE": 0x48,
        "INSERT": 0x49,
        "HOME": 0x4a,
        "PAGEUP": 0x4b,
        "DELETE": 0x4c,
        "END": 0x4d,
        "PAGEDOWN": 0x4e,
        "RIGHT": 0x4f,
        "LEFT": 0x50,
        "DOWN": 0x51,
        "UP": 0x52,
        "NUMLOCK": 0x53,
}

function = {
        "F1": 0x3a,
        "F2": 0x3b,
        "F3": 0x3c,
        "F4": 0x3d,
        "F5": 0x3e,
        "F6": 0x3f,
        "F7": 0x40,
        "F8": 0x41,
        "F9": 0x42,
        "F10": 0x43,
        "F11": 0x44,
        "F12": 0x45,
}

MODS = {k: 2**v for v, k in enumerate(
    ("LCTRL", "LSHIFT", "LALT", "LMETA",
     "RCTRR", "RSHIFT", "RART", "RMETA"))}

KEYS = {}
KEYS.update(letters)
KEYS.update(numbers)
KEYS.update(symbols_1)
KEYS.update(symbols_2)
KEYS.update(control)
KEYS.update(function)

KEYS_SHIFT = {}
KEYS_SHIFT.update(letters_shift)
KEYS_SHIFT.update(numbers_shift)
KEYS_SHIFT.update(symbols_1_shift)
KEYS_SHIFT.update(symbols_2_shift)

"""
KEYS = dict(
        **letters, **numbers,
        **symbols_1, **symbols_2,
        **control, **function
        )

KEYS_SHIFT = dict(
        **letters_shift, **numbers_shift,
        **symbols_1_shift, **symbols_2_shift
        )
"""
function_ext = {
        "\\F13\\": 0x68,
        "\\F14\\": 0x69,
        "\\F15\\": 0x6a,
        "\\F16\\": 0x6b,
        "\\F17\\": 0x6c,
        "\\F18\\": 0x6d,
        "\\F19\\": 0x6e,
        "\\F20\\": 0x6f,
        "\\F21\\": 0x70,
        "\\F22\\": 0x71,
        "\\F23\\": 0x72,
        "\\F24\\": 0x73,
}

keypad = {
        "\\KPSLASH\\": 0x54,
        "\\KPASTERISK\\": 0x55,
        "\\KPMINUS\\": 0x56,
        "\\KPPLUS\\": 0x57,
        "\\KPENTER\\": 0x58,
        "\\KP1\\": 0x59,
        "\\KP2\\": 0x5a,
        "\\KP3\\": 0x5b,
        "\\KP4\\": 0x5c,
        "\\KP5\\": 0x5d,
        "\\KP6\\": 0x5e,
        "\\KP7\\": 0x5f,
        "\\KP8\\": 0x60,
        "\\KP9\\": 0x61,
        "\\KP0\\": 0x62,
        "\\KPDOT\\": 0x63,
        "\\KPEQUAL\\": 0x67,
        "\\KPCOMMA\\": 0x85,
        "\\KPEQUAL\\": 0x86,
        "\\KPLEFTPAREN\\": 0xb6,
        "\\KPRIGHTPAREN\\": 0xb7,
}

other = {
        "\\102ND\\": 0x64,
        "\\COMPOSE\\": 0x65,
        "\\POWER\\": 0x66,
}

other_control = {
        "\\OPEN\\": 0x74,
        "\\HELP\\": 0x75,
        "\\PROPS\\": 0x76,
        "\\FRONT\\": 0x77,
        "\\STOP\\": 0x78,
        "\\AGAIN\\": 0x79,
        "\\UNDO\\": 0x7a,
        "\\CUT\\": 0x7b,
        "\\COPY\\": 0x7c,
        "\\PASTE\\": 0x7d,
        "\\FIND\\": 0x7e,
        "\\MUTE\\": 0x7f,
        "\\VOLUMEUP\\": 0x80,
        "\\VOLUMEDOWN\\": 0x81,
}

international = {
        "\\RO\\": 0x87,
        "\\KATAKANAHIRAGANA\\": 0x88,
        "\\YEN\\": 0x89,
        "\\HENKAN\\": 0x8a,
        "\\MUHENKAN\\": 0x8b,
        "\\KPJPCOMMA\\": 0x8c,
        "\\HANGEUL\\": 0x90,
        "\\HANJA\\": 0x91,
        "\\KATAKANA\\": 0x92,
        "\\HIRAGANA\\": 0x93,
        "\\ZENKAKUHANKAKU\\": 0x94,
}

other_modifier = {
        "\\LEFTCTRL\\": 0xe0,
        "\\LEFTSHIFT\\": 0xe1,
        "\\LEFTALT\\": 0xe2,
        "\\LEFTMETA\\": 0xe3,
        "\\RIGHTCTRL\\": 0xe4,
        "\\RIGHTSHIFT\\": 0xe5,
        "\\RIGHTALT\\": 0xe6,
        "\\RIGHTMETA\\": 0xe7,
}

media = {
        "\\PLAYPAUSE\\": 0xe8,
        "\\STOPCD\\": 0xe9,
        "\\PREVIOUSSONG\\": 0xea,
        "\\NEXTSONG\\": 0xeb,
        "\\EJECTCD\\": 0xec,
        "\\VOLUMEUP\\": 0xed,
        "\\VOLUMEDOWN\\": 0xee,
        "\\MUTE\\": 0xef,
        "\\WWW\\": 0xf0,
        "\\BACK\\": 0xf1,
        "\\FORWARD\\": 0xf2,
        "\\STOP\\": 0xf3,
        "\\FIND\\": 0xf4,
        "\\SCROLLUP\\": 0xf5,
        "\\SCROLLDOWN\\": 0xf6,
        "\\EDIT\\": 0xf7,
        "\\SLEEP\\": 0xf8,
        "\\COFFEE\\": 0xf9,
        "\\REFRESH\\": 0xfa,
        "\\CALC\\": 0xfb
}
