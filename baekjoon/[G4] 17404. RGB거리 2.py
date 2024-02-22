import sys

sys.stdin = open('input/17404-1.txt')  # 110, 3, 201, 208, 253
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * 3 for _ in range(n)]

answer = 1e9

for first in range(3):

    for j in range(3):
        if j == first:
            dp[0][j] = arr[0][j]
        else:
            dp[0][j] = 1e9

    for i in range(1, n):
        dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + arr[i][0]
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + arr[i][1]
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + arr[i][2]

    for j in range(3):
        if j != first:
            answer = min(answer, dp[n - 1][j])

print(answer)