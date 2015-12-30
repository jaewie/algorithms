from crypto import shift_char
from string import lowercase
from random import randint
from itertools import cycle, starmap, izip


def vigenere_cipher(msg, key):
    msg = msg.lower()
    letter_to_val = {char: val for val, char in enumerate(lowercase)}
    val_to_letter = {val: char for val, char in enumerate(lowercase)}

    get_val = lambda c0, c1: (
        letter_to_val[c0] + letter_to_val[c1]) % len(lowercase)
    get_cipher_char = lambda c0, c1: val_to_letter[get_val(c0, c1)]
    key = cycle(key)

    return ''.join(c for c in starmap(get_cipher_char, izip(msg, key)))


def one_time_pad(msg, pad=None):
    if pad is None:
        pad = (randint(0, len(lowercase) - 1) for _ in range(len(msg)))

    return ''.join(shift_char(char, shift) for char, shift in izip(msg, pad))


def caesar_cipher(text, shift):
    return ''.join(shift_char(c, shift) for c in text)
