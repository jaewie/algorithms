def max_subarray(lst):
    '''Return the maximum sum of a subarray in lst.'''

    max_ending_here = 0
    max_so_far = 0
    for num in lst:
        max_ending_here = max(0, max_ending_here + num)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far