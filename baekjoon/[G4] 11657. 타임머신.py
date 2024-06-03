import sys

sys.stdin = open('input/11657-1.txt')  # 4  3, -1, 3  -1
input = sys.stdin.readline

def bellman_ford():
    dist[1] = 0

    for i in range(N):
        for j in range(M):
            now, next, cost = edges[j]

            if dist[now] != 1e9 and dist[next] > dist[now] + cost:
                dist[next] = dist[now] + cost

                if i == N - 1:
                    return [-1]
    
    return dist[2:]

N, M = map(int, input().split())

edges = []
dist = [1e9] * (N + 1)

for _ in range(M):
    A, B, C = map(int, input().split())
    edges.append((A, B, C))

for i in bellman_ford():
    print(i if i != 1e9 else -1)