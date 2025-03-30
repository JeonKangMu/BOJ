import sys
from collections import deque

n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

queue = deque([(0,0,n,n)])
blue = 0
white = 0
while queue:
    rowStart, colStart, rowEnd, colEnd = queue.popleft()

    chk = arr[rowStart][colStart]
    flag = True
    for i in range(rowStart, rowEnd):
        for j in range(colStart, colEnd):
            if chk != arr[i][j]:
                flag = False
                break
        if not flag:
            break

    if flag:
        if chk == 1:
            blue += 1
        else:
            white += 1
    else:
        # 1사분면
        queue.append((rowStart, colStart, (rowStart + rowEnd) // 2, (colStart + colEnd) // 2))

        # 2사분면
        queue.append((rowStart, (colStart + colEnd) // 2, (rowStart + rowEnd) // 2, colEnd))

        # 3사분면
        queue.append(((rowStart + rowEnd) // 2, colStart, rowEnd, (colStart + colEnd) // 2))

        # 4사분면
        queue.append(((rowStart + rowEnd) // 2, (colStart + colEnd) // 2, rowEnd, colEnd))

print(white)
print(blue)
