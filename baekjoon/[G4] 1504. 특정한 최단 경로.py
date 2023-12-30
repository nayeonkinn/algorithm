import sys, heapq
sys.stdin = open('input/1504.txt')  # 7
input = sys.stdin.readline

def dijkstra(start):
    costs = [1e9] * (n + 1)
    queue = []

    costs[start] = 0
    heapq.heappush(queue, (0, start))

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

n, e = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

v1_route = dijkstra(1)[v1] + dijkstra(v1)[v2] + dijkstra(v2)[n]
v2_route = dijkstra(1)[v2] + dijkstra(v2)[v1] + dijkstra(v1)[n]

answer = min(v1_route, v2_route)
print(answer if answer < 1e9 else -1)