PRIME_MOD = 257
PRIME_BASE = 1000000007

def substr(s, sub):
    sub_hash = roll_hash(sub)
    check_hash = None
    for i in range(len(s) - len(sub) + 1):
        check = s[i:i + len(sub)]
        prev_char = s[i - 1] if i > 0 else None
        check_hash = roll_hash(check, prev_char, check_hash)
        
        if (roll_hash(check), check) == (sub_hash, sub):
            return i
    return -1

def roll_hash(s, prev_char=None, prev_hash=None, prime_mod=PRIME_MOD,
              prime_base=PRIME_BASE):
    if prev_hash is not None:
        return shift_hash_right(s, prev_hash, prev_char)

    k = len(s) - 1
    val = sum(ord(char) * prime_mod ** (k - i) for i, char in enumerate(s))
    return val % prime_base

def shift_hash_right(s, prev_hash, prev_char, prime_mod=PRIME_MOD,
              prime_base=PRIME_BASE):
    prev_hash -= ord(prev_char) * prime_mod ** (len(s) - 1)
    prev_hash *= prime_mod
    prev_hash += ord(s[-1])
    return prev_hash % prime_base