def bin_search(n, value):
    '''
    assume n is in order
    find the index of value in n
    otherwise return -1
    >>> bin_search([], 1)
    -1
    >>> bin_search([1], 1)
    0
    >>> bin_search([1], 2)
    -1
    >>> bin_search([11,22,33], 11)
    0
    >>> bin_search([11,22,33], 22)
    1
    >>> bin_search([11,22,33], 33)
    2
    >>> bin_search([11,22,33], 10)
    -1
    >>> bin_search([11,22,33], 20)
    -1
    >>> bin_search([11,22,33], 40)
    -1
    '''
    low = 0
    high = len(n) - 1
    while low <= high: # (1)
        mid = (low + high) // 2
        if value == n[mid]:
            return mid
        if value < n[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1

import doctest;doctest.testmod()