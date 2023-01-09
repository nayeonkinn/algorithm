import sys
sys.stdin = open('input/3184-1.txt') # 0 2, 3 1, 3 5
input = sys.stdin.readline

def bfs(i, j):
    global sheep, wolf

    sh = wo = 0
    queue = [(i, j)]
    visited[i][j] = 1
    while queue:
        i, j = queue.pop(0)
        if yard[i][j] == 'o':
            sh += 1
        elif yard[i][j] == 'v':
            wo += 1
        for di, dj in delta:
            ni, nj = di + i, dj + j
            if 0 <= ni < r and 0 <= nj < c and yard[ni][nj] != '#' and not visited[ni][nj]:
                queue.append((ni, nj))
                visited[ni][nj] = 1

    if sh > wo:
        sheep += sh
    else:
        wolf += wo

r, c = map(int, input().split())
yard = [list(input().strip()) for _ in range(r)]
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
visited = [[0] * c for _ in range(r)]
sheep = wolf = 0
for i in range(r):
    for j in range(c):
        if not visited[i][j] and yard[i][j] != '#':
            bfs(i, j)

print(sheep, wolf)
