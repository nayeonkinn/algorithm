import sys

sys.stdin = open('input/2606.txt')  # 4
input = sys.stdin.readline

def dfs(x):
    visited[x] = True

    for y in adj[x]:
        if not visited[y]:
            dfs(y)

N = int(input())
M = int(input())

adj = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())

    adj[a].append(b)
    adj[b].append(a)

dfs(1)

print(sum(visited) - 1)