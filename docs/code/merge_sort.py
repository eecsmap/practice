def merge_sort(data):
    temp = [None] * len(data)
    def merge(begin, mid, end):
        i, j = begin, mid
        k = begin
        while i < mid and j < end:
            if data[i] < data[j]:
                temp[k] = data[i]
                i += 1
                k += 1
            else:
                temp[k] = data[j]
                j += 1
                k += 1
        while i < mid:
            temp[k] = data[i]
            i += 1
            k += 1
        while j < end:
            temp[k] = data[j]
            j += 1
            k += 1
        data[begin:end] = temp[begin:end]
    def sort(begin, end):
        if begin >= end - 1: return
        mid = (begin + end) // 2
        sort(begin, mid)
        sort(mid, end)
        merge(begin, mid, end)
    sort(0, len(data))

sort = merge_sort

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