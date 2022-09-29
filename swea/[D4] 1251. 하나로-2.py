import sys
sys.stdin = open('input/1251.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    mst = [0] * N
    cost = [float('inf')] * N
    cost[0] = 0

    for _ in range(N):
        u = 0
        minV = float('inf')
        
        for i in range(N):
            if mst[i] == 0 and cost[i] < minV:
                u = i
                minV = cost[i]
        mst[u] = 1

        for v in range(N):
            if mst[v] == 0:
                d = ((X[u] - X[v]) ** 2 + (Y[u] - Y[v]) ** 2) * E
                cost[v] = min(d, cost[v])

    print(f'#{tc} {round(sum(cost))}')
