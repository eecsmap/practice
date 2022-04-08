def memoization(func):
    m = {}
    def wrapper(n, *args):
        if n not in m:
            m[n] = func(n, *args)
        return m[n]
    return wrapper

def fib(n):
    """
    return the nth number of fibonacci sequence.
    0 1 1 2 3 5 8 13
    >>> fib(5)
    5
    >>> fib(7)
    13
    >>> fib(50)
    12586269025
    """
    "YOUR CODE HERE"
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def gridTraverse(m, n):
    """
    in a m x n grid, you can only move up or right wards, 
    return how many possible paths you can make.
    >>> gridTraverse(1, 1)
    1
    >>> gridTraverse(2, 3)
    3
    >>> gridTraverse(4, 3)
    10
    >>> gridTraverse(18, 18)
    2333606220
    """
    "YOUR CODE HERE"

def canSum(n, numbers): 
    # Note that python stores default argument in Global Frame
    # So we can't simply call memo in the main function
    """
    given number n and a list numbers (all positive), return True is n
    can be summed by the elements in numbers, you can reuse
    elements in numbers.
    >>> canSum(7, [2, 3])
    True
    >>> canSum(7, [2, 3, 4, 7])
    True
    >>> canSum(7, [2, 4])
    False
    >>> canSum(300, [7, 14])
    False
    """
    "YOUR CODE HERE"

def howSum(n, numbers):
    """
    like the previous question, but this time
    return a list that adds to the given n, if
    the result contains multiple solution, return 
    any of the solutions
    >>> howSum(7, [2, 3])
    [3, 2, 2]
    >>> howSum(7, [5, 3, 4, 7])
    [4, 3]
    >>> howSum(8, [2, 3, 5])
    [2, 2, 2, 2]
    >>> howSum(7, [2, 3, 4, 7])
    [3, 2, 2]
    >>> howSum(7, [2, 4])
    >>> howSum(300, [7, 14])
    """
    "YOUR CODE HERE"

def bestSum(n, numbers):
    """
    like the previous question, this time, we have to
    return the answer list with minimum length
    >>> bestSum(7, [5, 3, 4, 7])
    [7]
    >>> bestSum(8, [2, 3, 5])
    [5, 3]
    >>> bestSum(8, [1, 4, 5])
    [4, 4]
    >>> bestSum(100, [1, 2, 5, 25])
    [25, 25, 25, 25]
    """
    "YOUR CODE HERE"

def canConstruct(target, wordBank):
    """
    given a string target, and a list of string wordBank,
    return True if target can be constructed by concatenating
    elements of the wordBank array.
    >>> canConstruct("abc", ["ab", "a", "bc"])
    True
    >>> canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
    True
    >>> canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    False
    >>> canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    True
    >>> canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    ... "e",
    ... "ee",
    ... "eee",
    ... "eeee",
    ... "eeeee",
    ... "eeeeee"
    ... ])
    False
    """
    "YOUR CODE HERE"

def countConstruct(target, wordBank):
    """
    like previous, return the number of ways to construct
    >>> countConstruct("abc", ["ab", "a", "bc"])
    1
    >>> countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"])
    1
    >>> countConstruct("purple", ["purp", "p", "ur", "le", "purpl"])
    2
    >>> countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    0
    >>> countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    4
    >>> countConstruct("eeeeee", ["e", "ee", "eee"])
    24
    >>> countConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])
    1623288080257
    >>> canConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    ... "e",
    ... "ee",
    ... "eee",
    ... "eeee",
    ... "eeeee",
    ... "eeeeee"
    ... ])
    0
    """
    "YOUR CODE HERE"

def allConstruct(target, wordBank):
    """
    like previous question, this time, return a 2-D array,
    which is composed of all the solutions for constructing the target
    >>> allConstruct("abcef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])
    [['ab', 'c', 'ef'], ['abc', 'ef']]
    >>> allConstruct("purple", ["purp", "p", "ur", "le", "purpl"])
    [['purp', 'le'], ['p', 'ur', 'p', 'le']]
    >>> allConstruct("aaaaa", ["a", "aa", "aaa"])
    [['a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'aa'], ['a', 'a', 'aa', 'a'], ['a', 'a', 'aaa'], ['a', 'aa', 'a', 'a'], ['a', 'aa', 'aa'], ['a', 'aaa', 'a'], ['aa', 'a', 'a', 'a'], ['aa', 'a', 'aa'], ['aa', 'aa', 'a'], ['aa', 'aaa'], ['aaa', 'a', 'a'], ['aaa', 'aa']]
    >>> allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    []
    """
    "YOUR CODE HERE"

def fib_tab(n):
    """
    return the nth number of fibonacci sequence.
    1 1 2 3 5 8 13
    >>> fib_tab(5)
    5
    >>> fib_tab(7)
    13
    >>> fib_tab(50)
    12586269025
    """
    "YOUR CODE HERE"
    
def gridTraverse_tab(m, n):
    """
    in a m x n grid, you can only move up or right wards, 
    return how many possible paths you can make.
    >>> gridTraverse_tab(1, 1)
    1
    >>> gridTraverse_tab(2, 3)
    3
    >>> gridTraverse_tab(4, 3)
    10
    >>> gridTraverse_tab(18, 18)
    2333606220
    """
    "YOUR CODE HERE"

def canSum_tab(n, numbers):
    """
    given number n and a list numbers (all positive), return True is n
    can be summed by the elements in numbers, you can reuse
    elements in numbers.
    >>> canSum_tab(7, [2, 3])
    True
    >>> canSum_tab(7, [2, 3, 4, 7])
    True
    >>> canSum_tab(7, [2, 4])
    False
    >>> canSum(300, [7, 14])
    False
    """
    "YOUR CODE HERE"

def howSum_tab(n, numbers):
    """
    like the previous question, but this time
    return a list that adds to the given n, if
    the result contains multiple solution, return 
    any of the solutions
    >>> howSum_tab(7, [2, 3])
    [3, 2, 2]
    >>> howSum_tab(7, [5, 3, 4, 7])
    [4, 3]
    >>> howSum_tab(8, [2, 3, 5])
    [2, 2, 2, 2]
    >>> howSum_tab(7, [2, 3, 4, 7])
    [3, 2, 2]
    >>> howSum_tab(7, [2, 4])
    >>> howSum_tab(300, [7, 14])
    """
    "YOUR CODE HERE"

def bestSum_tab(n, numbers):
    """
    like the previous question, this time, we have to
    return the answer list with minimum length
    >>> bestSum_tab(7, [5, 3, 4, 7])
    [7]
    >>> bestSum_tab(8, [2, 3, 5])
    [3, 5]
    >>> bestSum_tab(8, [1, 4, 5])
    [4, 4]
    >>> bestSum_tab(100, [1, 2, 5, 25])
    [25, 25, 25, 25]
    """
    "YOUR CODE HERE"

def canConstruct_tab(target, wordBank):
    """
    given a string target, and a list of string wordBank,
    return True if target can be constructed by concatenating
    elements of the wordBank array.
    >>> canConstruct_tab("abc", ["ab", "a", "bc"])
    True
    >>> canConstruct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"])
    True
    >>> canConstruct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    False
    >>> canConstruct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    True
    >>> canConstruct_tab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    ... "e",
    ... "ee",
    ... "eee",
    ... "eeee",
    ... "eeeee",
    ... "eeeeee"
    ... ])
    False
    """
    "YOUR CODE HERE"

def countConstruct_tab(target, wordBank):
    """
    like previous, return the number of ways to construct
    >>> countConstruct_tab("abc", ["ab", "a", "bc"])
    1
    >>> countConstruct_tab("abcdef", ["ab", "abc", "cd", "def", "abcd"])
    1
    >>> countConstruct_tab("purple", ["purp", "p", "ur", "le", "purpl"])
    2
    >>> countConstruct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    0
    >>> countConstruct_tab("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
    4
    >>> countConstruct_tab("eeeeee", ["e", "ee", "eee"])
    24
    >>> countConstruct_tab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"])
    1623288080257
    >>> countConstruct_tab("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", [
    ... "e",
    ... "ee",
    ... "eee",
    ... "eeee",
    ... "eeeee",
    ... "eeeeee"
    ... ])
    0
    """
    "YOUR CODE HERE"

def allConstruct_tab(target, wordBank):
    """
    like previous question, this time, return a 2-D array,
    which is composed of all the solutions for constructing the target
    >>> allConstruct_tab("abcef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"])
    [['ab', 'c', 'ef'], ['abc', 'ef']]
    >>> allConstruct_tab("purple", ["purp", "p", "ur", "le", "purpl"])
    [['purp', 'le'], ['p', 'ur', 'p', 'le']]
    >>> allConstruct_tab("aaaaa", ["a", "aa", "aaa"])
    [['a', 'a', 'a', 'a', 'a'], ['a', 'a', 'a', 'aa'], ['a', 'a', 'aa', 'a'], ['a', 'a', 'aaa'], ['a', 'aa', 'a', 'a'], ['a', 'aa', 'aa'], ['a', 'aaa', 'a'], ['aa', 'a', 'a', 'a'], ['aa', 'a', 'aa'], ['aa', 'aa', 'a'], ['aa', 'aaa'], ['aaa', 'a', 'a'], ['aaa', 'aa']]
    >>> allConstruct_tab("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
    []
    """
    "YOUR CODE HERE"