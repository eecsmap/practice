'''
cache holds at most m pages

read a page:
if the page is in the cache:
    touch the page
    return it from the cache
else:
    if the cache is full:
        evict the least recently used page then load the new page from the source
    else:
        load it from the source then return it from the cache

write a page:
if the page is in the cache:
    touch the page
    update the page in the cache
    if write_through:
        write it back to the source
else:
    if the cache is full:
        evict the least recently used page
    load the page from the source
    update the page in the cache
    if write through:
        write it back to the source

evict a page in the cache:
    if the page is dirty:
        write it back to the source
    remove the page from the cache

touch a page in the cache:
    update the page's last_accessed time
    move the page to the front of the cache

remove the least recently used page from the cache:
    remove the page from the cache
    return the page to the source

'''

from functools import lru_cache

@lru_cache(maxsize=3100)
def fib(n):
    '''
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(2)
    1
    >>> fib(3)
    2
    >>> fib(4)
    3
    >>> fib(5)
    5
    >>> fib(6)
    8
    >>> fib(7)
    13
    >>> fib(8)
    21
    >>> fib(9)
    34
    >>> fib(10)
    55
    >>> fib(506)
    2501848252103980047678723474640612996118441882248552061029655746089424880023811520697916190803488354459633
    '''
    assert n >= 0
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)

import doctest; doctest.testmod()


class LRU:

    def __init__(self, capacity):
        '''
        initialize the cache
        '''

    def touch(self, page_id):
        '''
        move the page to the front of the cache

        >>> lru = LRU(3)
        >>> lru.touch(5)
        None
        >>> lru.touch(6)
        None
        >>> lru.touch(7)
        None
        >>> lru.touch(5)
        None
        >>> lru.touch(8)
        6
        >>> lru.touch(7)
        None
        >>> lru.touch(9)
        5
        '''