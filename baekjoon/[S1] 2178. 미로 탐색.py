from collections import deque
import sys

sys.stdin = open('input/2178-1.txt')  # 15, 9, 38, 13
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [input().strip() for _ in range(N)]

visited = [[0] * M for _ in range(N)]
visited[0][0] = 1

q = deque([(0, 0)])

while q:
    i, j = q.popleft()

    if (i, j) == (N - 1, M - 1):
        break

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        ni, nj = i + di, j + dj

        if 0 <= ni < N and 0 <= nj < M and arr[ni][nj] == '1' and not visited[ni][nj]:
            visited[ni][nj] = visited[i][j] + 1
            q.append((ni, nj))

print(visited[-1][-1])