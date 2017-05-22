import string
from pprint import pprint as print
KEYS = {}
alphabet = {k: hex(v) for v, k in enumerate("abcdefghijklmnopqrstuvwxyz", start=4)}
numbers = {k: hex(v) for v, k in enumerate("1234567890", start=30)}
