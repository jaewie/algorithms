from string import lowercase


shift_char = lambda c, shift: lowercase[(lowercase.find(c) + shift) % len(lowercase)]
