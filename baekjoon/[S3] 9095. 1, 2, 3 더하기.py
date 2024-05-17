import sys

sys.stdin = open('input/9095.txt')  # 7  44  274
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())

    dp = [1, 2, 4] + [0] * (n - 3)

    for i in range(3, n):
        dp[i] += dp[i - 1] + dp[i - 2] + dp[i - 3]

    print(dp[n - 1])