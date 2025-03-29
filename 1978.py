import math

n = int(input())
arr = list(map(int, input().split()))
sarr = list(set(arr))

cnt = 0

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

for num in sarr:
    if is_prime(num):
        cnt += 1

print(cnt)