import sys
from collections import deque

sys.stdin = open('input/16946-1.txt')  # 303  050  303, 46003  00732  06040  50403
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().strip())) for _ in range(n)]

delta = ((1, 0), (-1, 0), (0, 1), (0, -1))
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if not arr[i][j] and not visited[i][j]:
            q = deque([(i, j)])
            visited[i][j] = True

            move = set()

            cnt = 0

            while q:
                x, y = q.popleft()
                cnt += 1
                
                for dx, dy in delta:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < m:
                        if arr[nx][ny]:
                            move.add((nx, ny))
                            continue
                        
                        if not arr[nx][ny] and not visited[nx][ny]:
                            visited[nx][ny] = True
                            q.append((nx, ny))
            
            for x, y in move:
                arr[x][y] += cnt

for i in range(n):
    print("".join(map(lambda x: str(x % 10), arr[i])))