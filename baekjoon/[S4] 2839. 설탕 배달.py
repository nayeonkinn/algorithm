import sys

sys.stdin = open('input/2839-1.txt')  # 4, -1, 2, 3, 3

N = int(input())

dp = [0] * (max(6, N + 1))
dp[3] = 1
dp[5] = 1

for i in range(6, N + 1):
    if dp[i - 5] and dp[i - 3]:
        dp[i] = min(dp[i - 5], dp[i - 3]) + 1
    elif dp[i - 5]:
        dp[i] = dp[i - 5] + 1
    elif dp[i - 3]:
        dp[i] = dp[i - 3] + 1

print(dp[N] if dp[N] else -1)