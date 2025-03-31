import sys

def binary_search(target, left, right):
    if left > right:
        return -1

    mid = (left + right) // 2

    if sarr[mid] == target:
        return mid
    elif sarr[mid] < target:
        return binary_search(target, mid + 1, right)
    else:
        return binary_search(target, left, mid - 1)

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sarr = sorted(set(arr))

for i in range(n):
    print(binary_search(arr[i], 0, len(sarr) - 1), end=' ')
