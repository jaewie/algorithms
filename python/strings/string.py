def substr(s, sub):
    sub_hash = roll_hash(sub)
    check_hash = None
    for i in range(len(s) - len(sub) + 1):
        check = s[i:i + len(sub)]
        prev_char = s[i - 1] if i > 0 else None
        check_hash = roll_hash(check, prev_char, check_hash)
        
        if roll_hash(check), check == sub_hash, sub:
            return i
    return -1

def roll_hash(s, prev_char=None, prev_hash=None, prime_mod=257,
              prime_base=1000000007):
    k = len(s) - 1
    if prev_hash is not None:
        return shift_hash_right(k, prev_hash, prev_char, prime_mod, prime_base)

    val = sum(ord(char) * prime_mod ** (k - i) for i, char in enumerate(s))
    return val % prime_base

def shift_hash_right(k, prev_hash, prev_char, prime_mod, prime_base):
    prev_hash -= ord(prev_char) * prime_mod ** (k)
    prev_hash *= prime_mod
    prev_hash += ord(k)
    return prev_hash % prime_base
