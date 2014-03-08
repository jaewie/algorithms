from crypto import shift_char
from itertools import izip
from string import lowercase
from random import randint


def one_time_pad(msg, pad=None):
  if pad is None:
    pad = (randint(0, len(lowercase)) for _ in range(len(msg)))

  return ''.join(shift_char(char, shift) for char, shift in izip(msg, pad))
