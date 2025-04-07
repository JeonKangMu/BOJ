import sys

e, s, m = map(int, sys.stdin.readline().split())

i, j, k = 1, 1, 1

cnt = 1

while e != i or s != j or m != k:
    i += 1
    j += 1
    k += 1

    if i == 16:
        i = 1

    if j == 29:
        j = 1

    if k == 20:
        k = 1

    cnt += 1

print(cnt)