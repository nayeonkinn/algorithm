import sys

sys.stdin = open('input/13141-1.txt')  # 9.0, 6.5
input = sys.stdin.readline

n, m = map(int, input().split())

dist = [[1e9] * n for _ in range(n)]
edges = []

for _ in range(m):
    s, e, l = map(int, input().split())
    s -= 1
    e -= 1

    dist[s][e] = dist[e][s] = min(dist[s][e], l)
    edges.append((s, e, l))

for i in range(n):
    dist[i][i] = 0

for i in range(n):
    for a in range(n):
        for b in range(n):
            dist[a][b] = min(dist[a][b], dist[a][i] + dist[i][b])

answer = 1e9

for i in range(n):
    time = 0

    for a, b, l in edges:
        time = max(time, (dist[a][i] + dist[b][i] + l) / 2)

    answer = min(answer, time)

print(answer)