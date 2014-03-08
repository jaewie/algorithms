from crypto import shift_char


def caesar_cipher(text, shift):
  return ''.join(shift_char(c) for c in text)
