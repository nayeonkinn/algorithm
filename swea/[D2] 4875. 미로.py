import sys
sys.stdin = open('input/4875.txt')

def findStart(maze):
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                return i, j

def backtrack(i, j):
    global answer
    for d in delta:
        di, dj = i + d[0], j + d[1]
        if 0 <= di < N and 0 <= dj < N:
            if maze[di][dj] == 0:
                maze[di][dj] = 1
                backtrack(di, dj)
            elif maze[di][dj] == 3:
                answer = 1
                return
    return

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

    answer = 0
    i, j = findStart(maze)
    backtrack(i, j)
    print(f'#{tc} {answer}')