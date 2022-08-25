import sys
sys.stdin = open('input/5102.txt', 'r')

def arrange(arr):
    way = [[] for _ in range(V + 1)]
    for a in arr:
        way[a[0]].append(a[1])
        way[a[1]].append(a[0])
    return way

def bfs(V, S, G):
    visited = [0] * (V + 1)
    visited[S] = 1
    queue = [S]

    while queue:
        v = queue.pop(0)
        if v == G:
            return visited[v] - 1
        for w in way[v]:
            if visited[w] == 0:
                visited[w] = visited[v] + 1
                queue.append(w)
    return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split()) # 노드 개수, 간선 개수
    way = arrange([list(map(int, input().split())) for _ in range(E)])
    S, G = map(int, input().split())
    print(f'#{tc} {bfs(V, S, G)}')