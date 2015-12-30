def permutations(lst):
    '''Return the permutation of lst.'''

    if len(lst) <= 1:
        return [lst]

    char = lst[0]
    perms = permutations(lst[1:])
    res = []
    for word in perms:
        for i in range(len(word) + 1):
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


def combs(lst, k):
    '''Return combinations of lst when choosing k.'''

    def _combs(pref, lst, k):
        if not k:
            return tuple(pref)

        new_lst = []
        for i in range(len(lst)):
            if k - 1 <= len(lst[i + 1:]):
                new_lst.append(_combs(pref + lst[i], lst[i + 1:], k - 1))
        return new_lst
    return flatten(_combs("", lst, k))


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


def group_sum(cur, rem, target):
    ''' Return if any combination of numbers in rem can sum up to target.'''

    if sum(cur) == target:
        return True
    if not rem:
        return False

    num = rem[0]

    return group_sum(cur + [num], rem[1:], target) or group_sum(
        cur, rem[1:], target)
