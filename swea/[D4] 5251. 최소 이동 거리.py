import sys
sys.stdin = open('input/5251.txt')

from collections import defaultdict
import heapq

T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    graph = defaultdict(list)
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    queue = [(0, 0)]
    dist = defaultdict(int)
    while queue:
        node, time = heapq.heappop(queue)
        if node not in dist:
            dist[node] = time
            for e, w in graph[node]:
                heapq.heappush(queue, (e, time + w))
    
    print(f'#{t} {dist[N]}')