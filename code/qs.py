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
    def _qs(lo, hi):
        if lo > hi: return
        pivot = data[hi]
        k = lo
        for i in range(lo, hi):
            if data[i] < pivot:
                data[k], data[i] = data[i], data[k]
                k += 1
        data[k], data[hi] = data[hi], data[k]
        _qs(lo, k - 1)
        _qs(k + 1, hi)
    _qs(0, len(data) - 1)

def test_quicksort():
    '''
    >>> data = [9,2,4,7,3,8,6,5,1]
    >>> quicksort(data)
    >>> data
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''

import doctest; doctest.testmod()
