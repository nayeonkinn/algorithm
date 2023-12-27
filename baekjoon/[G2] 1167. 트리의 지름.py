import sys
sys.stdin = open('input/1167.txt')  # 11
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(x, dist):
    global max_node, max_dist
    if dist > max_dist:
        max_node, max_dist = x, dist
    
    for y, d in info[x]:
        if not visited[y]:
            visited[y] = True
            dfs(y, dist + d)
            # visited[y] = False -> 트리이기 때문에 사이클 존재하지 않아 불필요

v = int(input())
info = [[] for _ in range(v + 1)]

for _ in range(v):
    i, *temp = list(map(int, input().split()))[:-1]
    for j in range(len(temp) // 2):
        info[i].append((temp[2 * j], temp[2 * j + 1]))

max_node, max_dist = None, 0

visited = [False] * (v + 1)
visited[1] = True
dfs(1, 0)

visited = [False] * (v + 1)
visited[max_node] = True
dfs(max_node, 0)

print(max_dist)