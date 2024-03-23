def quicksort(data):
    def _qs(begin, end):
        if end - begin < 2: return
        p = begin
        for i in range(begin, end):
            if data[i] <= data[end - 1]:
                data[i], data[p] = data[p], data[i]
                p += 1
        _qs(begin, p - 1)
        _qs(p, end)
    _qs(0, len(data))

def quicksort2(data):
    def _qs(first, last):
        if last - first < 1: return
        pivot = data[first]
        left, right = first, last
        while left <= right:
            while left <= right and data[left] <= pivot: left += 1
            while left <= right and data[right] >= pivot: right -= 1
            if left < right:
                data[left], data[right] = data[right], data[left]
                left += 1
                right -= 1
        data[first], data[right] = data[right], data[first]
        _qs(first, right - 1)
        _qs(right + 1, last)
    _qs(0, len(data) - 1)

quicksort = quicksort2


def quicksort(data):
    
    def _qs(begin, end):
        if end - begin < 2: return
        pivot = data[end-1]
        p = begin
        for k in range(begin, end):
            if data[k] < pivot:
                data[p], data[k] = data[k], data[p]
                p += 1
        data[p], data[end-1] = data[end-1], data[p]
        _qs(begin, p)
        _qs(p + 1, end)

    _qs(0, len(data))

def test_quicksort():
    '''
    >>> data = [9,2,4,7,3,8,6,5,1]
    >>> quicksort(data)
    >>> data
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''

import doctest; doctest.testmod()
