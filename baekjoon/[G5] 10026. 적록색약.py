from collections import deque
import sys

sys.stdin = open('input/10026.txt')  # 4 3
input = sys.stdin.readline

def bfs(i, j):
    q = deque([(i, j)])

    while q:
        x, y = q.popleft()

        for dx, dy in ((-1, 0), (0, -1), (1, 0), (0, 1)):
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and drawing[x][y] == drawing[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))

N = int(input())
drawing = [list(input().strip()) for _ in range(N)]

answer = [0, 0]

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            answer[0] += 1
            bfs(i, j)

for i in range(N):
    for j in range(N):
        if drawing[i][j] == 'R':
            drawing[i][j] = 'G'

visited = [[False] * N for _ in range(N)]
for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            answer[1] += 1
            bfs(i, j)

print(*answer)