import heapq
import sys
sys.stdin = open('input/1916.txt')  # 4
input = sys.stdin.readline

def dijkstra(start, end):
    queue = []
    heapq.heappush(queue, (0, start))

    costs = [1e9] * (n + 1)
    costs[start] = 0

    while queue:
        now_cost, now_node = heapq.heappop(queue)

        if now_cost > costs[now_node]:
            continue

        if now_node == end:  # 도착점 도착 시 종료
            return costs[now_node]

        for next_node, next_cost in graph[now_node]:
            cost = now_cost + next_cost

            if costs[next_node] > cost:
                costs[next_node] = cost
                heapq.heappush(queue, (cost, next_node))
    
    return costs[end]

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append((e, c))

a, b = map(int, input().split())

print(dijkstra(a, b))