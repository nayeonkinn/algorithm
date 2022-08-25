import sys
sys.stdin = open('input/1226.txt', 'r')

def find_start():
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                return i, j

def dfs(i, j):
    global answer
    if maze[i][j] == 3:
        answer = 1
        return
    visited[i][j] = 1

    for d in delta:
        di, dj = i + d[0], j + d[1]
        if 0 <= di < 16 and 0 <= dj < 16 and visited[di][dj] == 0 and maze[di][dj] != 1:
            visited[di][dj] = 1
            dfs(di, dj)
            visited[di][dj] = 0
    return

for tc in range(1, 11):
    input()
    maze = [list(map(int, list(input()))) for _ in range(16)]
    visited = [[0] * 16 for _ in range(16)]
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    answer = 0
    i, j = find_start()
    dfs(i, j)
    print(f'#{tc} {answer}')