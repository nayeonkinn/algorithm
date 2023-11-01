import sys
sys.stdin = open('input/1231-1.txt')  # 24, 100

c, d, m = map(int, input().split())
stocks = list(list(map(int, input().split())) for _ in range(c))

for i in range(d - 1):  # 기간
    dp = [0] * (m + 1)
    for j in range(c):  # 주식
        for k in range(stocks[j][i], m + 1):  # 자금
            dp[k] = max(dp[k], dp[k - stocks[j][i]] + stocks[j][i + 1] - stocks[j][i])
    dp += [0] * dp[m]
    m += dp[m]

print(m)
