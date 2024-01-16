import sys
import heapq

sys.stdin = open('input/1647.txt')  # 8
input = sys.stdin.readline


# 1. kruskal

n, m = map(int, input().split())
edges = sorted([list(map(int, input().split())) for _ in range(m)], key=lambda x: x[2])

parent = [i for i in range(n + 1)]

total_cost = 0
max_cost = 0

def union(a, b):
    a = find(a)
    b = find(b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])

    return parent[a]

for a, b, c in edges:
    if find(a) != find(b):
        union(a, b)
        total_cost += c
        max_cost = max(max_cost, c)

print(total_cost - max_cost)


# 2. prim

n, m = map(int, input().split())
edges = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    edges[a].append((b, c))
    edges[b].append((a, c))
visited = [False] * (n + 1)

q = []
heapq.heappush(q, (0, 1))

total_cost = 0
max_cost = 0

while q:
    now_cost, now_node = heapq.heappop(q)
    
    if not visited[now_node]:
        visited[now_node] = True
        total_cost += now_cost
        max_cost = max(max_cost, now_cost)

        for next_node, next_cost in edges[now_node]:
            if not visited[next_node]:
                heapq.heappush(q, (next_cost, next_node))

print(total_cost - max_cost)