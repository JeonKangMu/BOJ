import sys

def gcd(a, b):
    while b:
        a, b = b, a%b

    return a

n, m = map(int, sys.stdin.readline().split())

g = gcd(n, m)

print(g)
print(n * m // g)