import sys
sys.stdin = open('input/5105.txt', 'r')

def find_start(N):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def bfs(i, j, N):
    q = [(i, j)]
    v = [[0] * N for _ in range(N)]
    v[i][j] = 1

    while q:
        i, j = q.pop(0)
        for d in delta:
            di, dj = i + d[0], j + d[1]
            if 0 <= di < N and 0 <= dj < N and maze[di][dj] != 1 and v[di][dj] == 0:
                if maze[di][dj] == 3:
                    return v[i][j] - 1
                q.append((di, dj))
                v[di][dj] = v[i][j] + 1
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, list(input()))) for _ in range(N)]
    delta = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    i, j = find_start(N)
    print(f'#{tc} {bfs(i, j, N)}')