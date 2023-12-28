import sys, heapq
sys.stdin = open('input/1238.txt')  # 10
input = sys.stdin.readline

def dijkstra(start):
    queue = []
    costs = [1e9] * (n + 1)

    heapq.heappush(queue, (0, start))
    costs[start] = 0

    while queue:
        cost_now, node_now = heapq.heappop(queue)

        if costs[node_now] < cost_now:
            continue

        if start != x and node_now == x:  # x까지의 최소 거리 계산 완료 시 남은 노드 살펴보지 않고 함수 종료
            return costs

        for node_next, cost_next in info[node_now]:
            cost = cost_now + cost_next

            if costs[node_next] > cost:
                costs[node_next] = cost
                heapq.heappush(queue, (cost, node_next))
    
    return costs

n, m, x = map(int, input().split())
info = [[] for _ in range(n + 1)]
for _ in range(m):
    s, e, t = map(int, input().split())
    info[s].append((e, t))

dijkstra_x = dijkstra(x)  # x에서 돌아가는 거리 계산 (1회만 실행)

answer = 0
for i in range(1, n + 1):
    answer = max(answer, dijkstra(i)[x] + dijkstra_x[i])

print(answer)