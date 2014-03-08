from crypto import shift_char
from itertools import izip
from random import randint


def one_time_pad(msg, pad=None):
  if pad is None:
    pad = (randint(0, 25) for _ in range(len(msg)))

  return ''.join(shift_char(char, shift) for char, shift in izip(msg, pad))
