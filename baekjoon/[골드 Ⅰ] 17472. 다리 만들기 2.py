import sys
sys.stdin = open('input/17472-1.txt')


n, m = map(int, input().split())
land = [list(map(int, input().split())) for _ in range(n)]

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
visited = [[False] * m for _ in range(n)]
land_num = 1
for i in range(n):
    for j in range(m):
        if land[i][j] == 1 and visited[i][j] == False:
            queue = [(i, j)]
            visited[i][j] = True
            land[i][j] = land_num
            while queue:
                qi, qj = queue.pop(0)
                for di, dj in delta:
                    ni, nj = qi + di, qj + dj
                    if 0 <= ni < n and 0 <= nj < m and land[ni][nj] == 1 and visited[ni][nj] == False:
                        queue.append((ni, nj))
                        visited[ni][nj] = True
                        land[ni][nj] = land_num
            land_num += 1

for i in range(n):
    print(land[i])
