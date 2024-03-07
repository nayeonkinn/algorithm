import sys
from collections import deque

sys.stdin = open('input/20058-3.txt')  # 284  64, 280  64, 268  64, 248  62, 246  60, 37  9
input = sys.stdin.readline

N, Q = map(int, input().split())
n = 2 ** N
arr = [list(map(int, input().split())) for _ in range(n)]
sizes = list(map(lambda x: 2 ** int(x), input().split()))

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

for size in sizes:
    new_arr = [[0] * n for _ in range(n)]
    empty = []

    for i in range(0, n, size):
        for j in range(0, n, size):
            for x in range(size):
                for y in range(size):
                    if ice := arr[i + x][j + y]:
                        new_arr[i + y][j + size - 1 - x] = ice
                    else:
                        empty.append((i + y, j + size - 1 - x))

    arr = new_arr
    
    check = [[3] + [4] * (n - 2) + [3] for _ in range(n)]

    for i in range(n):
        check[0][i] -= 1
        check[n - 1][i] -= 1

    for x, y in empty:
        for dx, dy in delta:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < n:
                check[nx][ny] -= 1
    
    for i in range(n):
        for j in range(n):
            if check[i][j] < 3 and arr[i][j]:
                arr[i][j] -= 1
    
max_ice = 0
visited = [[False] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        if not visited[i][j] and arr[i][j]:
            visited[i][j] = True
            q = deque([(i, j)])
            ice = 0

            while q:
                x, y = q.popleft()

                ice += 1

                for dx, dy in delta:
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and arr[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))
            
            max_ice = max(max_ice, ice)

print(sum(map(sum, arr)))
print(max_ice)