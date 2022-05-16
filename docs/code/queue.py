class Queue:

    def __init__(self):
        self.data = []

    def is_empty(self):
        '''
        >>> queue = Queue()
        >>> queue.is_empty()
        True
        '''
        return len(self.data) == 0
    
    def push(self, value):
        '''
        >>> queue = Queue()
        >>> queue.push(1)
        >>> queue.is_empty()
        False
        '''
        self.data.append(value)

    def pop(self):
        '''
        >>> queue = Queue()
        >>> queue.push(1)
        >>> queue.push(2)
        >>> queue.pop()
        1
        >>> queue.pop()
        2
        >>> queue.is_empty()
        True
        '''
        return self.data.pop(0)

class Queue2:

    def __init__(self):
        self.data = []

    def is_empty(self):
        '''
        >>> queue = Queue2()
        >>> queue.is_empty()
        True
        '''
        return len(self.data) == 0
    
    def push(self, value):
        '''
        >>> queue = Queue2()
        >>> queue.push(1)
        >>> queue.is_empty()
        False
        '''
        self.data.insert(0, value)

    def pop(self):
        '''
        >>> queue = Queue2()
        >>> queue.push(1)
        >>> queue.push(2)
        >>> queue.pop()
        1
        >>> queue.pop()
        2
        >>> queue.is_empty()
        True
        '''
        return self.data.pop()

class Node:

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class Queue3:

    def __init__(self):
        self.tail = None

    def is_empty(self):
        '''
        >>> queue = Queue()
        >>> queue.is_empty()
        True
        '''
        return self.tail == None
    
    def push(self, value):
        '''
        >>> queue = Queue3()
        >>> queue.push(1)
        >>> queue.is_empty()
        False
        '''
        if self.tail == None:
            self.tail = Node(value)
            self.tail.next = self.tail
        else:
            self.tail.next = Node(value, self.tail.next)
        self.tail = self.tail.next

    def pop(self):
        '''
        >>> queue = Queue3()
        >>> queue.push(1)
        >>> queue.push(2)
        >>> queue.pop()
        1
        >>> queue.pop()
        2
        >>> queue.is_empty()
        True
        '''
        if self.is_empty():
            raise ValueError('queue is empty')
        head = self.tail.next
        value = head.value
        if head.next == head:
            self.tail = None
        else:
            self.tail.next = head.next
        return value

import time
import timeit

n = 1000000
start = time.process_time_ns()
queue = Queue()
for i in range(n):
    queue.push(i)
print('average push: ', (time.process_time_ns() - start) / n)

start = time.process_time_ns()
while not queue.is_empty():
    queue.pop()
print('average pop: ', (time.process_time_ns() - start) / n)
