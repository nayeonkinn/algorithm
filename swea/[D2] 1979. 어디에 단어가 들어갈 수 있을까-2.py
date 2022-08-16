import sys
sys.stdin = open('input/1979.txt', 'r')

T = int(input())
for t in range(T) :
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0
    for i in range(N):
        row = col = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                row += 1
            if puzzle[j][i] == 1:
                col += 1

            if puzzle[i][j] == 0 or j == N - 1:
                if row == K:
                    cnt += 1
                row = 0
            if puzzle[j][i] == 0 or j == N - 1:
                if col == K:
                    cnt += 1
                col = 0

    print(f'#{t + 1} {cnt}')