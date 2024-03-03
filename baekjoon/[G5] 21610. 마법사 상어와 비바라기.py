import sys

sys.stdin = open('input/21610-1.txt')  # 77, 41, 2657
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

dx = (0, 0, -1, -1, -1, 0, 1, 1, 1)
dy = (0, -1, -1, 0, 1, 1, 1, 0, -1)

cloud = [(n - 2, 0), (n - 2, 1), (n - 1, 0), (n - 1, 1)]
visited = [[False] * n for _ in range(n)]

for _ in range(m):
    d, s = map(int, input().split())

    cloud = list(map(lambda x: ((x[0] + dx[d] * s) % n, (x[1] + dy[d] * s) % n), cloud))

    for cx, cy in cloud:
        visited[cx][cy] = True

    for cx, cy in cloud:
        cnt = 0
        for i in range(2, 9, 2):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < n and (arr[nx][ny] or visited[nx][ny]):
                cnt += 1

        arr[cx][cy] += cnt + 1

    cloud = []
    
    for x in range(n):
        for y in range(n):
            if arr[x][y] >= 2 and not visited[x][y]:
                arr[x][y] -= 2
                cloud.append((x, y))
            visited[x][y] = False

print(sum(map(sum, arr)))