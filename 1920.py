import sys

def binary_search(target, data_list, left, right):
    if left > right:
        return None

    mid = (left + right) // 2

    if data_list[mid] == target:
        return mid
    elif data_list[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

    return binary_search(target, data_list, left, right)

n = int(sys.stdin.readline())
nlist = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
mlist = list(map(int, sys.stdin.readline().split()))

nlist.sort()

for i in mlist:
    if binary_search(i, nlist, 0, len(nlist) - 1) != None:
        print("1")
    else:
        print("0")