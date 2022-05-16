# Independency

If we have:

$$P(A) \cdot P(B) = P(A,B)$$

$$P(A) = P(A|B)$$

We say that $A$ is independent with $B$, as $A \perp B$


```py
import random

def sample():
    a_done = False
    count = 0
    while not a_done:
        a = random.random() < 0.5
        count += 1
        #print(a, b)
        if count == 1:
            old_a = a
        else:
            if a != old_a: a_done = True
    return count

n = 100000
print(sum(sample() for i in range(n)) / n)
```

```py
def sample():
    a_done = False
    b_done = False
    count = 0
    while not a_done or not b_done:
        a = random.random() < 0.5
        b = random.random() < 0.5
        count += 2
        #print(a, b)
        if count == 2:
            old_a = a
            old_b = b
        else:
            if a != old_a: a_done = True
            if b != old_b: b_done = True
    return count

n = 1000000
print(sum(sample() for i in range(n)) / n)
```

```py
def sample():
    a_done = False
    b_done = False
    count = 0
    while not a_done and not b_done:
        a = random.random() < 0.5
        b = random.random() < 0.5
        count += 2
        #print(a, b)
        if count == 2:
            old_a = a
            old_b = b
        else:
            if a != old_a: a_done = True
            if b != old_b: b_done = True
    return count

n = 1000000
print(sum(sample() for i in range(n)) / n)
```

$|\Omega| = 52 \times 51 \times 50 \times 49 \times 48$

$$P[X=1] = 0$$
123456789abcd
11112
11122
11222
12222


$$P[X=2] = \frac{\binom{52}{1} \binom{51}{1} \binom{50}{1} \binom{49}{1} \binom{48}{1} (2^5 - 2)}{\frac{52!}{(52-5)!}}$$

ABCDE
$$P[X=5] = \frac{13 * 12 * 11 * 10 * 9 * 4^5}{52 * 51 * 50 * 49 * 48}$$

ABCDA
ABCDB
ABCDC
ABCDD

$$P[X=4] = \frac{13*12*11*10*4*4^4}{52 * 51 * 50 * 49 * 48}$$

ABCAA
ABCAB
ABCAC
ABCBA
ABCBB
ABCBC
ABCCA
ABCCB
ABCCC
$$P[X=3] = \frac{13*12*11*3^2*4^4}{52 * 51 * 50 * 49 * 48}$$
