import sys
import heapq

sys.stdin = open('input/1197.txt')  # 3
input = sys.stdin.readline

def union(x, y):
    x = find(x)
    y = find(y)

    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    
    return parent[x]

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]
edges = []
answer = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    heapq.heappush(edges, (cost, a, b))

while edges:
    cost, a, b = heapq.heappop(edges)

    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)