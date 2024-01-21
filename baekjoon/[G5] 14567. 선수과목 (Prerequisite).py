import sys
from collections import deque

sys.stdin = open('input/14567-1.txt')  # 1 2 3, 1 2 2 1 3 1
input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

q = deque()

answer = [0] * n

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if not indegree[i]:
        q.append((i, 1))

while q:
    x, cnt = q.popleft()

    answer[x - 1] = cnt

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            q.append((y, cnt + 1))

print(*answer)