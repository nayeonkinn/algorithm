import sys, heapq
sys.stdin = open('input/1753.txt')  # 0 2 3 7 INF
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))

    costs = [1e9] * (V + 1)
    costs[start] = 0

    while queue:
        now_cost, now_node = heapq.heappop(queue)

        if now_cost > costs[now_node]:
            continue

        for next_node, next_cost in graph[now_node]:
            cost = now_cost + next_cost
            if cost < costs[next_node]:
                costs[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
    
    return costs

V, E = map(int, input().split())
K = int(input())

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

for i in dijkstra(K)[1:]:
    print(i) if i < 1e9 else print('INF')