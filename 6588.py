import sys
import math

p = [True] * 1000001
p[0] = False
p[1] = False

for i in range(2, int(math.sqrt(1000001)) + 1):
    if p[i]:
        for j in range(i * i, 1000001, i):
            p[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break

    for i in range(3, n // 2 + 1, 2):
        if p[i] and p[n - i]:
            print(f"{n} = {i} + {n - i}")
            break