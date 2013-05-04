def rem_duplicates(lst):

    hit = [False for i in range(256)]      
    hit[ord(lst[0])] = True
    tail = 1
    
    for i in range(1, len(lst)):
        val = ord(lst[i])
        if not hit[val]:
            lst[tail] = lst[i]
            tail += 1
            hit[val] = True
    
    if tail != len(lst):
        lst[tail] = '\0'
    return lst

def is_anagrams(a, b):
    
    a_count = {}
    b_count = {}
    
    for char in a:
        a_count[char] = a_count.get(char, 0) + 1
        
    for char in b:
        b_count[char] = b_count.get(char, 0) + 1
        
    if len(a_count) != len(b_count):
        return False
    
    for char in a_count:
        b_num = b_count.get(char, None)
        if a_count[char] != b_num:
            return False
    return True

def permutation(string):
    return _permute([c for c in string])
    
def _permute(lst):
    
    if len(lst) <= 1:
        return lst
    
    char = lst[0]
    perms = _permute(lst[1:])
    new_perms = []
    for word in perms:
        for j in range(len(word) + 1):
            new_perms.append(_insert(word, char, j))
    return new_perms

def _insert(str1, char, ind):
    
    a = list(str1)
    a.insert(ind, char)
    
    return ''.join(a)

def largest_block(s):
    if not s:
        return -1
    if len(s) == 1:
        return 0
    
    i = 0
    largest_count = [0, 0]
    boo = True
    
    while i < len(s) - 1:
        
        if boo:
            cur_count = [i, 0]
            boo = False
        
        if s[i] == s[i+1]:
            cur_count[1] += 1
        else:
            boo = True
            if cur_count[1] > largest_count[1]:
                largest_count = cur_count
        i += 1
    
    if cur_count[1] > largest_count[1]:
        largest_count = cur_count
        
    return largest_count[0]

