import random
import math
from Crypto.Util.number import *

p = getPrime(15)
q_list = []
for i in range (1, p):
    if (p-1) % i == 0:
        k = 0
        for j in range(2, i // 2 + 1):
            if (i % j == 0):
                k = k + 1
        if (k <= 0):
            q_list.append(i)

print(q_list)
q = max(q_list)
print("______________________________________________________")
print("p = ", p)
print("q = ", q)
print("______________________________________________________")
z_list = []
for z in range (1, p):
    if (z**q) % p == 1:
        z_list.append(z)
print(z_list)
g = max(z_list)
print("g = ", g)
print("______________________________________________________")
max_t = math.log2(q)
t = random.randint(1, math.floor(max_t))
e = random.randint(1, 2**t)
print("t = ", t)
print("e = ", e)
print("______________________________________________________")
a = random.randint(1, q-1)
r = random.randint(1, q)
print("a = ", a)
print("r = ", r)
