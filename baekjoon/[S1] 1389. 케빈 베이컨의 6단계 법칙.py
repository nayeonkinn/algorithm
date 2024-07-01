from collections import deque
import sys

sys.stdin = open('input/1389.txt')  # 3
input = sys.stdin.readline

n, m = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

min_val = 1e9

for i in range(1, n + 1):
    q = deque([i])
    dist = [0] * (n + 1)
    dist[i] = 1

    while q:
        j = q.popleft()

        for k in adj[j]:
            if not dist[k]:
                dist[k] = dist[j] +  1
                q.append(k)
        
    if sum(dist) < min_val:
        min_val = sum(dist)
        answer = i

print(answer)