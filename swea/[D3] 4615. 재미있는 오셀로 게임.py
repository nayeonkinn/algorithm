import sys
sys.stdin = open('input/4615.txt', 'r')

def change(i, j, di, dj, bw):
    if i == di:
        for k in range(min(j, dj) + 1, max(j, dj)):
            board[i][k] = bw
    elif j == dj:
        for k in range(min(i, di) + 1, max(i, di)):
            board[k][j] = bw
    elif (i - di) * (j - dj) > 0:
        for k in range(min(i, di) + 1, max(i, di)):
            board[k][k - i + j] = bw
    else:
        for k in range(min(i, di) + 1, max(i, di)):
            board[k][i + j - k] = bw 

def check(i, j, bw):
    for d in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        for k in range(1, N):
            di, dj = i + d[0] * k, j + d[1] * k
            if 0 <= di < N and 0 <= dj < N:
                if board[di][dj] == 0:
                    break
                if board[i][j] == board[di][dj]:
                    change(i, j, di, dj, bw)
                    break

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [[0] * N for _ in range(N)]
    board[N // 2 - 1][N // 2 - 1:N // 2 + 1] = [2, 1]
    board[N // 2][N // 2 - 1:N // 2 + 1] = [1, 2]

    for _ in range(M):
        j, i, bw = map(int, input().split())
        board[i - 1][j - 1] = bw
        check(i - 1, j - 1, bw)

    b = w = 0
    for i in range(N):
        b += board[i].count(1)
        w += board[i].count(2)
    print(f'#{tc} {b} {w}')