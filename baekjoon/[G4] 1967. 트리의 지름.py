import sys
sys.stdin = open('input/1967.txt')  # 45
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(now, diameter):
    global max_node, max_dist

    if max_dist < diameter:
        max_dist = diameter
        max_node = now

    for next, dist in graph[now]:
        if not visited[next]:
            visited[next] = True
            dfs(next, diameter + dist)

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

max_node, max_dist = 0, 0  # max_node = None으로 설정할 경우 n이 1일 때 visited[None]이 되어 오류 발생

visited = [False] * (n + 1)
visited[1] = True
dfs(1, 0)

visited = [False] * (n + 1)
visited[max_node] = True
dfs(max_node, 0)

print(max_dist)