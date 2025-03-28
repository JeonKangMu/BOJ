import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [[] for _ in range(n + 1)]
parent = [0] * (n + 1)

for i in range(n-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque([1])
parent[1] = 1

while queue:
    current = queue.popleft()
    for child in graph[current]:
        if parent[child] == 0:
            parent[child] = current
            queue.append(child)

for i in range(2, n+1):
    print(parent[i])