def quick_sort(data):

    def _partition1(start, end):
        '''
        from CLRS: chapter 7
        '''
        pivot = data[end]
        i = start - 1
        for j in range(start, end):
            if data[j] <= pivot: # < could work as well, actually I prefer to use <
                i += 1
                data[i], data[j] = data[j], data[i]
        data[end], data[i + 1] = data[i + 1], data[end]
        return i + 1

    def _partition2(start, end):
        '''
        from Problem Solving with Algorithms and Data Structures Using Python
        '''
        pivot = data[start]
        done = False
        i = start + 1
        j = end
        while not done:
            while i <= j and data[i] <= pivot: i += 1 # must be <= and >= to get meet
            while i <= j and data[j] >= pivot: j -= 1
            if i > j: done = True
            else:
                data[i], data[j] = data[j], data[i] # if pivot on begin, use j to indicate the pos
        data[j], data[start] = data[start], data[j]
        return j

    def _partition25(start, end):
        '''
        from Problem Solving with Algorithms and Data Structures Using Python
        '''
        pivot = data[end]
        done = False
        i = start
        j = end - 1
        while not done:
            while i <= j and data[i] <= pivot: i += 1
            while i <= j and data[j] >= pivot: j -= 1
            if i > j: done = True
            else:
                data[i], data[j] = data[j], data[i] # if pivot on end, use i to indicate the pos
        data[i], data[end] = data[end], data[i]
        return i

    def _partition3(start, end):
        '''
        my thought
        '''
        i = start
        for j in range(start + 1, end + 1):
            if data[j] < data[start]:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[start], data[i] = data[i], data[start]
        return i
    
    import random
    _partition = [_partition1, _partition2, _partition3][random.randint(0, 2)]
    
    def _quick_sort(start, end):
        if start >= end: return
        p = _partition(start, end)
        _quick_sort(start, p - 1)
        _quick_sort(p + 1, end)

    _quick_sort(0, len(data) - 1)


def qsort(data):
    '''
    practice
    '''
    def _qsort(first, last):
        if first >= last: return
        pivot = data[first]
        p = first
        for i in range(first + 1, last + 1):
            if data[i] <= pivot:
                p += 1
                data[p], data[i] = data[i], data[p]
        data[first], data[p] = data[p], data[first]
        _qsort(first, p - 1)
        _qsort(p + 1, last)

    return _qsort(0, len(data) - 1)

sort = qsort #quick_sort

def test_sort():
    '''
    >>> data = [2, 4, 6, 9, 7, 8, 5, 3, 1]
    >>> sort(data)
    >>> data
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> data = []
    >>> sort(data)
    >>> data
    []
    >>> data = [1]
    >>> sort(data)
    >>> data
    [1]
    >>> data = [1,2]
    >>> sort(data)
    >>> data
    [1, 2]
    >>> data = [1,2,3]
    >>> sort(data)
    >>> data
    [1, 2, 3]
    >>> data = [2,1]
    >>> sort(data)
    >>> data
    [1, 2]
    >>> data = [3,2,1]
    >>> sort(data)
    >>> data
    [1, 2, 3]
    '''

import doctest; doctest.testmod()