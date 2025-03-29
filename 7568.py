n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

rank = [1]*n
for i in range(n):
    for j in range(n):
        if arr[j][0] > arr[i][0] and arr[j][1] > arr[i][1]:
            rank[i]+=1

for i in range(n):
    print(rank[i], end=" ")