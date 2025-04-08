import sys

n = int(sys.stdin.readline())

cnt = 0
idx = 1
div = 10

while n % div != n:
    for _ in range(9):
        cnt += idx * (div//10)
    div *= 10
    idx += 1

n = n - div//10

for i in range(n + 1):
    cnt += idx

print(cnt)