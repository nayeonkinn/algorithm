import sys, heapq

sys.stdin = open('input/11179.txt')   # 4  3  1 3 5
input = sys.stdin.readline

n = int(input())
m = int(input())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

start, end = map(int, input().split())

d = [1e9] * (n + 1)
d[start] = 0
hq = [(0, [start])]

while hq:
    cost, route = heapq.heappop(hq)

    if route[-1] == end:
        print(cost)
        print(len(route))
        print(*route)
        break

    for next_city, next_cost in adj[route[-1]]:
        if cost + next_cost < d[next_city]:
            d[next_city] = cost + next_cost
            heapq.heappush(hq, (cost + next_cost, route + [next_city]))