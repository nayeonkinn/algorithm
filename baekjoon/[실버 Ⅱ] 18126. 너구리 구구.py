import sys
sys.stdin = open('input/18126.txt')


import heapq

N = int(input())
visited = [False] * (N + 1)
adj = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    fr, to, d = map(int, input().split())
    adj[fr].append((d, to))
    adj[to].append((d, fr))

queue = []
heapq.heappush(queue, (1, 1))
visited[1] = 1
while queue:
    fr_d, fr = heapq.heappop(queue)
    for to_d, to in adj[fr]:
        if not visited[to] or visited[to] > fr_d + to_d:
            heapq.heappush(queue, (fr_d + to_d, to))
            visited[to] = fr_d + to_d

print(max(visited) - 1)
