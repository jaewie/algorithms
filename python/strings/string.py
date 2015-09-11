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

def match(text, pat):
    # Knuth-Morris-Pratt!
    pi = get_pi(pat)
    matched = 0
    i = 0

    while i < len(text):
        t, p = text[i + matched], pat[matched]

        if t == p:
            matched += 1
        else:
            i += matched - pi[matched]
            matched = 0

        if matched == len(pat):
            return i
    return -1

def get_pi(s):
    k = -1
    pi = {0: k}

    for i, c in enumerate(s, 1):
        while k >= 0 and s[k] != c:
            k = pi[k]
        k += 1
        pi[i] = k

    return pi
