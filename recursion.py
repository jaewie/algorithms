def permutations(lst):
    '''Return the permutation of lst.'''

    if len(lst) <= 1:
        return [lst]
    
    char = lst[0]
    perms = permutations(lst[1:])
    res = []
    for word in perms:
        for i in range(len(word)+1):
            res.append(_insert(word, char, i))
    return res

def _insert(word, char, i):
    '''Insert string char into string word at index i.'''

    word = list(word)
    word.insert(i, char)
    return tuple(word)

def power_set(s):
    '''Return the powerset of s.'''

    lst = []
    for i in range(len(s) + 1):
        lst += comb("", s, i)
    return lst

def flatten(lst):
    '''Flatten the list lst.'''

    res = []
    
    for item in lst:
        if isinstance(item, list):
            res += flatten(item)
        else:
            res.append(item)
    return res

def combs(lst, k):
    '''Return combinations of lst when choosing k.'''

    def _combs(pref, lst, k):
        if not k:
            return tuple(pref)
            
        new_lst = []
        for i in range(len(lst)):
            if k-1 <= len(lst[i+1:]):
                new_lst.append(_combs(pref+lst[i], lst[i+1:], k-1))
        return new_lst
    return flatten(_combs("", lst, k))

def recursive_BST(lst, lo, hi, x):
    '''Return the index of x in lst. Return -1 if it is not in lst'''
    
    if lo > hi:
        return -1
    
    mid = (lo + hi) / 2
    
    if lst[mid] == x:
        return mid
    elif lst[mid] < x:
        lo = mid + 1
    else:
        hi = mid - 1
    return recursive_BST(lst, lo, hi, x)

def get_phone_words(number, pref):
    '''Return all possible words for a given phone number.'''

    if not number:
        return pref
    letter_lookup = {"2": "ABC",
                     "3": "DEF",
                     "4": "GHI",
                     "5": "JKL",
                     "6": "MND",
                     "7": "PRS",
                     "8": "TUV",
                     "9": "WXY"}
    res = []
    
    num = number[0]
    for letter in letter_lookup[num]:
        res.append(get_phone_words(number[1:], pref + letter))
    return res

def dice_ways(count, lst, x):
    ''' Count number of ways a dice with n faces (values of lst) can sum up
    to x.'''

    if count == x:
        return 1
    if not lst:
        return 0

    num = lst[0]
    tot = 0
    for i in range(1, num+1):
        if count + i <= x:
            tot += dice_ways(count + i, lst[1:], x)
    tot += dice_ways(count, lst[1:], x)
    return tot

def group_sum(cur, rem, target):
    ''' Return if any combination of numbers in rem can sum up to target.'''
    
    if sum(cur) == target:
        return True
    if not rem:
        return False
    
    num = rem[0]
    
    return group_sum(cur+[num], rem[1:], target) or group_sum(
        cur, rem[1:], target)

def recursive_pset(s):
    ''' Return the powerset of string s.'''

    if not s:
        return [""]
    
    char = s[0]
    sets = recursive_pset(s[1:])
    res = []
    res.extend(recursive_pset(s[1:]))
    for st in sets:
        res.append(st + char)
    return res
