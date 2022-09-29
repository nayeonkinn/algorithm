import sys
sys.stdin = open('input/5251.txt')

def dijkstra(v):
    U = [0] * (N + 1)
    U[v] = 1
    D = [0] * (N + 1)
    for i in range(N + 1):
        D[i] = adj[v][i]

    for _ in range(N + 1):
        minV, w = 10000, 0
        for i in range(N + 1):
            if U[i] == 0 and D[i] < minV:
                minV, w = D[i], i
        U[w] = 1

        for v in range(N + 1):
            if 0 < adj[w][v] < 11:
                D[v] = min(D[w] + adj[w][v], D[v])

    return D[N]

T = int(input())
for tc in range(1, T + 1):
    N, E = map(int, input().split())
    adj = [[11] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        s, e, w = map(int, input().split())
        adj[s][e] = w
    for i in range(N + 1):
        adj[i][i] = 0
    print(f'#{tc} {dijkstra(0)}')
