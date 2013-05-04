def permutations(lst):
    
    if len(lst) <= 1:
        return lst
    
    char = lst[0]
    perms = permutations(lst[1:])
    res = []
    for word in perms:
        for i in range(len(word)+1):
            res.append(_insert(word, char, i))
    return res

def _insert(word, char, i):
    word = lst(word)
    word.insert(i, char)
    return tuple(word)


def comb(prefix, list, count):
    if count is 0:
        return [prefix]
    lst = []
    for i in range (len(list)):
        lst += comb(prefix +list[i], list[i+1:], count - 1)
    return lst

def power_set(s):
    
    lst = []
    for i in range(len(s) + 1):
        lst += comb("", s, i)
    return lst
    
def combs(pref, lst, k):
    
    if not k:
        return tuple(pref)
    
    
    new_lst = []
    for i in range(len(lst)):
        
        if k-1 <= len(lst[i+1:]):
            new_lst.append(combs(pref+lst[i], lst[i+1:], k-1))
    return new_lst

