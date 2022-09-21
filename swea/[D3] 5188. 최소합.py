import sys
sys.stdin = open('input/5188.txt')

def dfs(i, j, total):
    global min_total
    if (i, j) == (N - 1, N) or (i, j) == (N, N - 1):
        min_total = min(total, min_total)
        return

    if i < N and j < N:
        dfs(i + 1, j, total + arr[i][j])
        dfs(i, j + 1, total + arr[i][j])

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_total = 10 * 13 * 13
    dfs(0, 0, 0)
    print(f'#{t} {min_total}')
