from random import random as r
from math import floor

def sample(n, m):
    data = [0 for i in range(m)]
    for i in range(n):
        data[floor(r() * m)] += 1
    return (data[0], data[1])

xs = {}
ys = {}
xys = {}
n = 6
m = 4
for i in range(1000000):
    x, y = sample(n, m)
    if x not in xs: xs[x] = 0
    xs[x] += 1
    if y not in ys: ys[y] = 0
    ys[y] += 1
    if x * y not in xys: xys[x * y] = 0
    xys[x * y] += 1

print('E(X) = ', sum(v * f for v, f in xs.items()) / sum(xs.values()))
print('E(Y) = ', sum(v * f for v, f in ys.items()) / sum(ys.values()))
print('E(XY) = ', sum(v * f for v, f in xys.items()) / sum(xys.values()))
print((m - 1) / (m) + (n-1)/2)