def hanoi(n):
    '''
    return moves as a list of tuples
    to move n pieces from pole1 to pole2
    with help of pole3
    >>> hanoi(0)
    >>> hanoi(1)
    [(1, 2)]
    >>> hanoi(2)
    [(1, 3), (1, 2), (3, 2)]
    '''
    if n <= 0: return None
    moves = []
    def helper(src, dst, temp, count):
        if count == 1:
            moves.append((src, dst))
        else:
            helper(src, temp, dst, count-1)
            moves.append((src, dst))
            helper(temp, dst, src, count-1)
    helper(1, 2, 3, n)
    return moves

import doctest; doctest.testmod()
