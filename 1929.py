import math

m, n = map(int, input().split())

for i in range(m, n + 1):
    flag = True
    if i < 2:
        continue

    for j in range(2, int(math.sqrt(i)) + 1):
        if i % j == 0:
            flag = False
            break

    if flag:
        print(i)