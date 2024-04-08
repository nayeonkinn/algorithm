import sys

sys.stdin = open('input/3687.txt')  # 7 7  6 111  8 711  108 7111111

INF = float('inf')

num = [INF, INF, 1, 7, 4, 2, 0, 8]
dp = num + [INF] * 93
dp[6] = 6

for i in range(8, 101):
    for j in range(2, 8):
        dp[i] = min(dp[i], dp[i - j] * 10 + num[j])

for _ in range(int(input())):
    n = int(input())

    # 최소값 (DP)
    print(dp[n], end=' ')

    # 최대값 (그리디)
    if n % 2:
        print('7' + '1' * (n // 2 - 1))
    else:
        print('1' * (n // 2))