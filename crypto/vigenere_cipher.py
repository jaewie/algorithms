from string import lowercase
from itertools import cycle, starmap, izip


def vigenere_cipher(msg, key):
  msg = msg.lower()
  letter_to_val = {char: val for val, char in enumerate(lowercase)}
  val_to_letter = {val: char for val, char in enumerate(lowercase)}

  get_val = lambda c0, c1: (letter_to_val[c0] + letter_to_val[c1]) % len(lowercase)
  get_cipher_char = lambda c0, c1: val_to_letter[get_val(c0, c1)]
  key = cycle(key) if len(msg) > len(key) else key

  return ''.join(c for c in starmap(get_cipher_char, izip(msg, key)))
