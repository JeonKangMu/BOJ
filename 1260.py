import sys
from collections import deque
n, m, v = map(int, sys.stdin.readline().split())

arr = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n + 1):
    arr[i].sort()

visited = [False] * (n + 1)

def dfs(v):
    visited[v] = True
    print(v, end=' ')

    for vertex in arr[v]:
        if not visited[vertex]:
            dfs(vertex)

def bfs(v):
    queue = deque([v])
    visited[v] = True

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')

        for vertex2 in arr[vertex]:
            if not visited[vertex2]:
                visited[vertex2] = True
                queue.append(vertex2)

dfs(v)
for i in range(n+1):
    visited[i] = False
print("")
bfs(v)