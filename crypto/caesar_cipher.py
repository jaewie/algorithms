from crypto import shift_char


def caesar_cipher(text, shift):
  return ''.join(shift_char(c, shift) for c in text)
