def rem_duplicates(lst):
    '''Remove any duplicates in lst.'''

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
    '''Return whether string a and b are anagrams.'''

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

def first_non_repeated_char(string):
    '''Return the first non repeated character in string.'''

    d = {}
    
    for char in string:
        if d.get(char):
            d[char] = "Repeated"
        else:
            d[char] = "First"
    
    for char in string:
        if d[char] == "First":
            return char
    return -1
