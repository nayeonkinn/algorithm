import heapq
import sys

sys.stdin = open('input/1766.txt')  # 3 1 4 2
input = sys.stdin.readline

n, m = map(int, input().split())

edges = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)

q = []
answer = []

for _ in range(m):
    a, b = map(int, input().split())
    edges[a].append(b)
    indegree[b] += 1

for i in range(1, n + 1):
    if not indegree[i]:
        heapq.heappush(q, i)
    
while q:
    a = heapq.heappop(q)
    answer.append(a)

    for b in edges[a]:
        indegree[b] -= 1

        if not indegree[b]:
            heapq.heappush(q, b)

print(*answer)