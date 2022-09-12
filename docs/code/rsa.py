import math
import subprocess

cmd = ('openssl prime -generate -bits 512')
prime = lambda: int(subprocess.check_output(cmd, shell=True).strip())
p = prime()
q = prime()
N = p * q
M = (p - 1) * (q - 1)
e = 65537
assert math.gcd(e, M) == 1
d = pow(e, -1, M)
x = 1234567890
y = pow(x, e, N)
print('y =', y)
z = pow(y, d, N)
print('z =', z)
assert x == z
