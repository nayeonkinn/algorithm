import sys, heapq

sys.stdin = open('input/1854.txt')  # -1  10  7  5  14
input = sys.stdin.readline

n, m, k = map(int, input().split())

adj = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    adj[a].append((b, c))

d = [[1e9] * k for _ in range(n + 1)]
d[1][0] = 0
hq = [(0, 1)]

while hq:
    cost, city = heapq.heappop(hq)
    
    if cost > d[city][-1]:
        continue

    for next_city, next_cost in adj[city]:
        if cost + next_cost < d[next_city][-1]:
            d[next_city][-1] = cost + next_cost
            d[next_city].sort()
            heapq.heappush(hq, (cost + next_cost, next_city))

for i in range(1, n + 1):
    print(-1 if d[i][k - 1] == 1e9 else d[i][k - 1])