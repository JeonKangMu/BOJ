import sys

n, m = map(int, sys.stdin.readline().split())

visited = [False] * (n + 1)
arr = []

def dfs(depth):
    if depth == m:
        print(*arr)
        return

    for i in range(1, n + 1):
        if visited[i] == False:
            visited[i] = True
            arr.append(i)
            dfs(depth + 1)
            arr.pop()
            visited[i] = False

dfs(0)