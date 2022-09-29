import sys
sys.stdin = open('input/5250.txt')

import heapq

def dijkstra(i, j):
    cost = [[1000 * 100 * 100] * N for _ in range(N)]
    cost[0][0] = 0
    queue = [(0, 0, 0)]

    while queue:
        c, i, j = heapq.heappop(queue)

        for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            di += i
            dj += j
            if 0 <= di < N and 0 <= dj < N:
                fuel = H[di][dj] - H[i][j] + 1 if H[i][j] < H[di][dj] else 1
                if c + fuel < cost[di][dj]:
                    cost[di][dj] = c + fuel
                    heapq.heappush(queue, (cost[di][dj], di, dj))

    return cost[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    H = [list(map(int, input().split())) for _ in range(N)]
    print(f'#{tc} {dijkstra(0, 0)}')
