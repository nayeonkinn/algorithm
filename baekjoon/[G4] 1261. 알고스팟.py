import heapq, sys

sys.stdin = open('input/1261-1.txt')  # 3, 0, 2
input = sys.stdin.readline

m, n = map(int, input().split())
arr = [list(map(int, list(input().strip()))) for _ in range(n)]

hq = [(0, 0, 0)]
dist = [[10000] * m for _ in range(n)]
dist[0][0] = 0

while hq:
    i, j, cnt = heapq.heappop(hq)

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj

        if 0 <= ni < n and 0 <= nj < m:
            next_cnt = cnt + arr[ni][nj]

            if  next_cnt < dist[ni][nj]:
                dist[ni][nj] = next_cnt
                heapq.heappush(hq, (ni, nj, next_cnt))

print(dist[-1][-1])