import sys
from collections import deque

sys.stdin = open('input/2623.txt')  # 6  2  1  5  4  3, 0, 0
input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

q = deque()
visited = []

for _ in range(m):
    k, *order = list(map(int, input().split()))

    for i in range(k - 1):
        edges[order[i]].append(order[i + 1])
        indegree[order[i + 1]] += 1

for i in range(1, n + 1):
    if not indegree[i]:
        q.append(i)

while q:
    x = q.popleft()
    visited.append(x)

    for y in edges[x]:
        indegree[y] -= 1

        if not indegree[y]:
            q.append(y)

if len(visited) == n:
    print(*visited, sep='\n')
else:
    print(0)