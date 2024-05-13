import sys

sys.stdin = open('input/1937.txt')  # 4
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(i, j):
    if not dp[i][j]:
        dp[i][j] = 1

        for di, dj in ((0, -1), (0, 1), (-1, 0), (1, 0)):
            ni, nj = i + di, j + dj

            if 0 <= ni < n and 0 <= nj < n and bamboo[ni][nj] > bamboo[i][j]:
                dp[i][j] = max(dp[i][j], dfs(ni, nj) + 1)
    
    return dp[i][j]

n = int(input())
bamboo = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        dfs(i, j)

print(max(map(max, dp)))