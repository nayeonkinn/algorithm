import sys
sys.stdin = open('input/4615.txt', 'r')

def check(i, j, bw):
    for d in [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]:
        change = []
        for k in range(1, N):
            di, dj = i + d[0] * k, j + d[1] * k
            if 0 <= di < N and 0 <= dj < N:
                if board[di][dj] == 0:
                    break
                elif board[i][j] == board[di][dj]:
                    for c in change:
                        board[c[0]][c[1]] = bw
                    break
                else:
                    change.append((di, dj))

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