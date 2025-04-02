import sys
n = int(sys.stdin.readline())

divisors = [0] * (1000001)
for i in range(1, 1000001):
    for j in range(i, 1000001, i):
        divisors[j] += i

g = [0] * (1000001)
for i in range(1, 1000001):
    g[i] = g[i-1] + divisors[i]

for i in range(n):
    print(g[int(sys.stdin.readline())])