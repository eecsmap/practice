# Data Structure

## Basic Data Structures

## Basic Algorithms

```
def bin_search(n, value):
    '''
    assume n is in order
    find the index of value in n
    otherwise return -1
    >>> bin_search([1,2,3], 1)
    0
    >>> bin_search([1,2,3], 2)
    1
    >>> bin_search([1,2,3], 3)
    2
    >>> bin_search([], 1)
    -1
    >>> bin_search([1], 1)
    0
    >>> bin_search([1], 2)
    -1
    '''
    low = 0
    high = len(n) - 1
    while low <= high:
        mid = (low + high) // 2
        if value == n[mid]:
            return mid
        if value < n[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
```