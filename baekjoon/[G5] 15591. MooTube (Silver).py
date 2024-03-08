from collections import deque
import sys

sys.stdin = open('input/15591.txt')  # 3  0  2
input = sys.stdin.readline

def bfs(k, v):
    dq = deque([v])
    visited = [False] * (n + 1)
    visited[v] = True
    answer = 0

    while dq:
        v = dq.popleft()
        for w, usado in graph[v]:
            if not visited[w] and usado >= k:
                visited[w] = True
                dq.append(w)
                answer += 1
                
    print(answer)

n, q = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b, usado = map(int, input().split())
    graph[a].append((b, usado))
    graph[b].append((a, usado))

for _ in range(q):
    k, v = map(int, input().split())
    bfs(k, v)