from string import lowercase

def caesar_cipher(text, shift):
  shift_char = lambda c: lowercase[(lowercase.find(c) + shift) % len(lowercase)]

  return ''.join(shift_char(c) for c in text)

