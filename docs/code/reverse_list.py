class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next
    def __repr__(self):
        return f'({self.value}, {self.next})'

def get_link(list):
    link = None
    for i in list[::-1]:
        link = Node(i, link)
    return link

def reverse_link(link):
    '''
    >>> reverse_link(get_link([]))
    >>> reverse_link(get_link([1]))
    (1, None)
    >>> reverse_link(get_link([1, 2, 3]))
    (3, (2, (1, None)))
    '''
    prev, curr, next = None, link, link.next if link else None
    while curr:
        prev_prev = prev
        prev, curr, next = curr, next, next.next if next else None
        prev.next = prev_prev
    return prev
