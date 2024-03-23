def sa0(s):
    ans = [i for i in range(len(s))]
    def qs(begin, end):
        if end - begin < 2: return
        p = begin
        for i in range(begin, end):
            if s[ans[i]:] <= s[ans[end - 1]:]:
                ans[p], ans[i] = ans[i], ans[p]
                p += 1
        qs(begin, p - 1)
        qs(p, end)
    qs(0, len(s))
    return ans

def sa1(s):
    ans = [i for i in range(len(s))]
    ans.sort(key=lambda i: s[i:])
    return ans

def sa2(s):
    return sorted((i for i in range(len(s))), key=lambda x: s[x:])

sa = sa2

def test():
    '''
    >>> sa('ponoiiipoi')
    [9, 4, 5, 6, 2, 8, 3, 1, 7, 0]
    '''

import doctest; doctest.testmod()