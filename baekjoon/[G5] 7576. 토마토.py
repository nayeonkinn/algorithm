from collections import deque
import sys

sys.stdin = open('input/7576-1.txt')  # 8, -1, 6, 14, 0
input = sys.stdin.readline

m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))

while q:
    i, j = q.popleft()

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj

        if 0 <= ni < n and 0 <= nj < m and not box[ni][nj]:
            box[ni][nj] = box[i][j] + 1
            q.append((ni, nj))

if all(map(all, box)):
    print(max(map(max, box)) - 1)
else:
    print(-1)