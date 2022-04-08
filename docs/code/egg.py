def balloon_tab(numbers):
    '''
    >>> balloon_tab([1,2,3])
    12
    >>> balloon_tab([4,5,7])
    175
    >>> balloon_tab([2,3,100,4])
    1412
    '''
    return 

def balloon(numbers):
    '''
    >>> balloon([1,2,3])
    12
    >>> balloon([4,5,7])
    175
    >>> balloon([2,3,100,4])
    1412
    '''
    if len(numbers) == 1:
        return numbers[0]
    if len(numbers) == 2:
        return numbers[0] * numbers[1] + max(numbers)
    return max(balloon(numbers[:i] + numbers[i+1:]) + value(numbers, i) for i in range(len(numbers)))

def value(numbers, i):
    v = numbers[i]
    if i > 0:
        v *= numbers[i - 1]
    if i < len(numbers) - 1:
        v *= numbers[i + 1]
    return v