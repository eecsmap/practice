import math
import subprocess

cmd = ('openssl prime -generate -bits 512')
prime = lambda: int(subprocess.check_output(cmd, shell=True).strip())

p = prime()
q = prime()

N = p * q
M = (p - 1) * (q - 1)

# find e such that e coprime to M
e = 65537
assert math.gcd(e, M) == 1

# find d such that e * d = 1 mod M, inverse of e mod M
d = pow(e, -1, M)

# x is the message to be encrypted
x = 1234567890
# y is the encrypted message
y = pow(x, e, N)
print('y =', y)
# z is the decrypted message
z = pow(y, d, N)
print('z =', z)
# make sure z is the same as x
assert x == z

# e, d are exchangable for encryption and decryption
y = pow(x, d, N)
print('y =', y)
z = pow(y, e, N)
print('z =', z)
assert x == z
