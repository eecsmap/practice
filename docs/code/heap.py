class Heap:

    def __init__(self):
        self.data = [None]

    def is_empty(self):
        '''
        >>> heap = Heap()
        >>> heap.is_empty()
        True
        >>> heap.push(1, 'a')
        >>> heap.is_empty()
        False
        '''
        return len(self.data) == 1

    def push(self, key, value):
        '''
        >>> heap = Heap()
        >>> heap.data
        [None]
        >>> heap.push(0, 0)
        >>> heap.data
        [None, (0, 0)]
        >>> heap.push(1, 1)
        >>> heap.data
        [None, (1, 1), (0, 0)]
        >>> heap.push(3, 3)
        >>> heap.data
        [None, (3, 3), (0, 0), (1, 1)]
        >>> heap.push(2, 2)
        >>> heap.data
        [None, (3, 3), (2, 2), (1, 1), (0, 0)]
        '''
        self.data.append((key, value))
        self._up(len(self.data) - 1)
    
    def pop(self):
        '''
        >>> heap = Heap()
        >>> for i in [0,1,2,3,4,5,6,7,8,9]: heap.push(i, i)
        >>> [heap.pop()[0] for i in range(10)]
        [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
        '''
        assert len(self.data) > 1, self.data
        last = self.data.pop()
        if len(self.data) == 1:
            return last
        value = self.data[1]
        self.data[1] = last
        self._down(1)
        return value
    
    def _up_recusive(self, i):
        parent = i >> 1
        if parent and self.data[parent][0] < self.data[i][0]:
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            self._up_recusive(parent)

    def _up_iterative(self, i):
        parent = i >> 1
        while parent and self.data[parent][0] < self.data[i][0]:
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            i, parent = parent, parent >> 1
    
    _up = _up_iterative
    
    def _down_recusive(self, i):
        n = len(self.data) - 1
        left_child, right_child = i << 1, (i << 1) + 1
        largest = i
        if left_child <= n and self.data[left_child][0] > self.data[largest][0]:
            largest = left_child
        if right_child <= n and self.data[right_child][0] > self.data[largest][0]:
            largest = right_child
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self._down_recusive(largest)

    def _down_iterative(self, i):
        left_child, right_child = i << 1, (i << 1) + 1
        n = len(self.data) - 1
        while i <= n:
            largest = i
            if left_child <= n and self.data[left_child][0] > self.data[largest][0]:
                largest = left_child
            if right_child <= n and self.data[right_child][0] > self.data[largest][0]:
                largest = right_child
            if largest == i:
                return
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            i, left_child, right_child = largest, largest << 1, (largest << 1) + 1

    _down = _down_iterative

    def remove(self, i):
        self.data[i] = self.data[-1]
        self.n -= 1
        self.up(i)
        self.down(i)

def test_heap_random():
    import random
    heap = Heap()
    data = list(range(100))
    random.shuffle(data)
    for i in data:
        heap.push(i, i)
    output = []
    for i in range(len(data)):
        output.append(heap.pop())
    for i, j in zip(range(99, 0, -1), output):
        assert i == j[0]

test_heap_random()
