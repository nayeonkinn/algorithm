import sys
sys.stdin = open('input/11725-1.txt')  # 4 6 1 3 1 4, 1 1 2 3 3 4 4 5 5 6 6
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node):
    for n in graph[node]:
        if not visited[n]:
            visited[n] = True
            parent[n] = node
            dfs(n)

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [None] * (n + 1)
visited = [False] * (n + 1)

dfs(1)

for p in parent[2:]:
    print(p)