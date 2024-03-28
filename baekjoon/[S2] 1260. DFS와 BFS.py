from collections import deque
import sys

sys.stdin = open('input/1260-1.txt')  # 1 2 4 3  1 2 3 4, 3 1 2 5 4  3 1 4 2 5, 1000 999  1000 999
input = sys.stdin.readline

def dfs(v):
    visited[v] = True
    answer.append(v)

    for w in adj[v]:
        if not visited[w]:
            dfs(w)

def bfs(v):
    visited[v] = True
    q = deque([v])

    while q:
        v = q.popleft()
        answer.append(v)

        for w in adj[v]:
            if not visited[w]:
                visited[w] = True
                q.append(w)

n, m, v = map(int, input().split())
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

adj = list(map(sorted, adj))

answer = []
visited = [False] * (n + 1)
dfs(v)
print(*answer)

answer = []
visited = [False] * (n + 1)
bfs(v)
print(*answer)