import sys

sys.stdin = open('input/1520.txt')  # 3
input = sys.stdin.readline

def dfs(i, j):
    if dp[i][j] != -1:
        return dp[i][j]

    if i == m - 1 and j == n - 1:
        return 1
    
    cnt = 0

    for di, dj in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        ni, nj = i + di, j + dj

        if 0 <= ni < m and 0 <= nj < n and arr[i][j] > arr[ni][nj]:
            cnt += dfs(ni, nj)
    
    dp[i][j] = cnt

    return dp[i][j]

m, n = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]

dp = [[-1] * n for _ in range(m)]

print(dfs(0, 0))