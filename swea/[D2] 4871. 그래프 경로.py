import sys
sys.stdin = open('input/4871.txt', 'r')

def dfs(v):
    stack = [v]
    visited[v] = 1

    while stack:
        for w in road[v]:
            if visited[w] == 0:
                if w == end:
                    return 1
                v = w
                visited[v] = 1
                stack.append(v)
                break
        else:
            stack.pop()
            if stack :
                v = stack[-1]
            else:
                return 0

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    road = [[] for _ in range(V + 1)]
    for e in range(E):
        t1, t2 = map(int, input().split())
        road[t1].append(t2)
    start, end = map(int, input().split())

    visited = [0] * (V + 1)
    print(f'#{tc} {dfs(start)}')