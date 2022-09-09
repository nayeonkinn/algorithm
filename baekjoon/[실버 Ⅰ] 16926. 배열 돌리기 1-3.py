import sys
sys.stdin = open('input/16926-1.txt')

from collections import deque

N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for i in range(min(N, M) // 2):
    q = deque()

    x, y = i, i
    for di, dj, ji, jj in ((1, 0, -1, 1), (0, 1, -1, -1), (-1, 0, 1, -1), (0, -1, 1, 1)):
        while i <= x < N - i and i <= y < M - i:
            q.append(arr[x][y])
            x += di
            y += dj
        x += ji
        y += jj

    q.pop()
    q.rotate(R)

    x, y = i, i
    for di, dj, ji, jj in ((1, 0, -1, 1), (0, 1, -1, -1), (-1, 0, 1, -1), (0, -1, 1, 1)):
        while i <= x < N - i and i <= y < M - i and q:
            arr[x][y] = q.popleft()
            x += di
            y += dj
        x += ji
        y += jj

for i in range(N):
    print(*arr[i])