# https://www.acwing.com/problem/content/142/

def sa(s):
    '''
    >>> sa('ponoiiipoi')
    [9, 4, 5, 6, 2, 8, 3, 1, 7, 0]
    '''
    return sorted((range(len(s))), key=lambda x: s[x:])

import doctest; doctest.testmod()
