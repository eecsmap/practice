class Stack:

    def __init__(self, data=None):
        self.data = []
        if data:
            for i in data:
                self.push(i)
        
    def push(self, v):
        self.data.append(v)
    
    def pop(self):
        return self.data.pop()
    
    def __len__(self):
        return len(self.data)
    
    def __iter__(self):
        while self:
            yield self.pop()
