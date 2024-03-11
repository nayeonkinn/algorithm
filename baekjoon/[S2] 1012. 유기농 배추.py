from collections import deque
import sys

sys.stdin = open('input/1012-1.txt')  # 5  1, 2
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())

    arr = [[False] * m for _ in range(n)]
    visited = [[False] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        arr[y][x] = True

    answer = 0

    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:
                answer += 1
                visited[i][j] = True
                q = deque([(i, j)])

                while q:
                    x, y = q.popleft()

                    for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                        nx, ny = x + dx, y + dy

                        if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
    
    print(answer)