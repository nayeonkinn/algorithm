import sys

sys.stdin = open('input/17484.txt')  # 29
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(lambda x: [int(x)] * 3, input().split())) for _ in range(n)]

for i in range(n):
    dp[i][0][0] = 1000
    dp[i][m - 1][2] = 1000

for i in range(1, n):
    for j in range(m):
        if j != 0:
            dp[i][j][0] += min(dp[i - 1][j - 1][1], dp[i - 1][j - 1][2])
        dp[i][j][1] += min(dp[i - 1][j][0], dp[i - 1][j][2])
        if j != m - 1:
            dp[i][j][2] += min(dp[i - 1][j + 1][0], dp[i - 1][j + 1][1])

print(min(map(min, dp[-1])))