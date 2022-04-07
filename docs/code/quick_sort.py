def quick_sort(data):

    def _partition1(start, end):
        '''
        from CLRS: chapter 7
        '''
        pivot = data[end]
        i = start - 1
        for j in range(start, end):
            if data[j] <= pivot: # (1)
                i += 1
                data[i], data[j] = data[j], data[i]
        data[end], data[i + 1] = data[i + 1], data[end]
        return i + 1

    def _partition2(start, end):
        '''
        from book:
        Problem Solving with Algorithms and Data Structures Using Python
        '''
        assert start < end
        pivot = data[start]
        i = start + 1
        j = end
        # loop invariant:
        # data on the left side of i are <= pivot
        # data on the right side of j are >= pivot
        while i <= j:
            while i <= j and data[i] <= pivot: i += 1 # (2)
            while i <= j and data[j] >= pivot: j -= 1
            if i < j:
                data[i], data[j] = data[j], data[i]
        assert j < i
        # since pivot is at the begining, swap with j
        # if we have choosen pivot at the end, then swap with i
        data[j], data[start] = data[start], data[j]
        return j

    def _partition3(start, end):
        '''
        Another example using end pivot
        '''
        pivot = data[end]
        i = start
        j = end - 1
        while i <= j:
            while i <= j and data[i] <= pivot: i += 1
            while i <= j and data[j] >= pivot: j -= 1
            if i < j:
                data[i], data[j] = data[j], data[i]
        data[i], data[end] = data[end], data[i]
        return i

    def _partition4(start, end):
        '''
        my way
        '''
        i = start
        for j in range(start + 1, end + 1):
            if data[j] < data[start]:
                i += 1
                data[i], data[j] = data[j], data[i]
        data[start], data[i] = data[i], data[start]
        return i
    
    def _partition5(start, end):
        '''
        Hoare-partition
        '''
        i = start
        pivot = data[end]
        for j in range(start, end):
            # loop invariant holds before each iteration
            assert all(d < pivot for d in data[:i])
            if data[j] < pivot:
                data[i], data[j] = data[j], data[i]
                i += 1
            # loop invariant holds after each iteration
            assert all(d < pivot for d in data[:i])
        # now all items in data[start:end] are organized into two parts
        # from data[start:i] are < pivot
        # from data[i:end] are >= pivot
        # then we swap data[i] with data[end]
        # return i as the partition point
        data[i], data[end] = data[end], data[i]
        return i
    
    def _partition6(start, end):
        '''
        Hoare-partition variant, to save the last swap
        The cost is to protentially move more items unnecesary
        '''
        i = start
        pivot = data[end]
        for j in range(start, end + 1):
            # loop invariant holds before each iteration
            assert all(d <= pivot for d in data[:i])
            if data[j] <= pivot:
                data[i], data[j] = data[j], data[i]
                i += 1
            # loop invariant holds after each iteration
            assert all(d <= pivot for d in data[:i])
        # now all items in data[start:end] are organized into two parts
        # from data[start:i] are <= pivot
        # data[i - 1] == pivot
        # from data[i+1:end] are > pivot
        return i - 1

    _partition = _partition6
    
    def _quick_sort(start, end):
        if start >= end: return
        p = _partition(start, end)
        _quick_sort(start, p - 1)
        _quick_sort(p + 1, end)

    _quick_sort(0, len(data) - 1)


def qsort(data):
    def _qsort(begin, end):
        if end - begin < 2: return
        p = begin
        for i in range(begin, end):
            if data[i] <= data[end - 1]:
                data[p], data[i] = data[i], data[p]
                p += 1
        _qsort(begin, p - 1)
        _qsort(p, end)
    return _qsort(0, len(data))

sort = qsort 
#sort = quick_sort

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