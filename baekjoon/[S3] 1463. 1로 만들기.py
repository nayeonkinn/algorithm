import sys

sys.stdin = open('input/1463-1.txt')  # 1, 3

X = int(input())

dp = [0] * (X + 1)

for i in range(2, X + 1):
    dp[i] = dp[i - 1] + 1

    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[-1])