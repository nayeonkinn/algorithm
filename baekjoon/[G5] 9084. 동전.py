import sys

sys.stdin = open('input/9084.txt')  # 501  121  1
input = sys.stdin.readline

for _ in range(int(input())):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())

    dp = [0] * (M + 1)
    dp[0] = 1

    for coin in coins:
        for i in range(coin, M + 1):
            dp[i] += dp[i - coin]

    print(dp[-1])