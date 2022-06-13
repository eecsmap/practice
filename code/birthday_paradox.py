import math, random

def experiment(total, m, n):
    ncollision = 0
    for i in range(total):
        if trial(m, n):
            ncollision += 1
    print(ncollision / total)

def trial(m, n):
    s = set()
    for i in range(m):
        sample = math.floor(random.random() * n)
        if sample in s:
            return True
        s.add(sample)
    return False

experiment(100000, 22, 365)