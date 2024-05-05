import heapq, sys

sys.stdin = open('input/18352-1.txt')  # 4, -1, 2  3
input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

hq = [(0, x)]
dist = [1e9] * (n + 1)

while hq:
    d, node = heapq.heappop(hq)

    if d > k:
        continue

    if d < dist[node]:
        dist[node] = d

        for next_node in graph[node]:
            heapq.heappush(hq, (d + 1, next_node))

if answer := [i for i, v in enumerate(dist) if v == k]:
    for x in answer:
        print(x)
else:
    print(-1)