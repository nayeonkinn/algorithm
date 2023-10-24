import sys
sys.stdin = open('input/17208-3.txt')  # 2, 1, 3

n, m, k = map(int, input().split())
orders = [list(map(int, input().split())) for _ in range(n)]

dp = [[[0] * (k + 1) for _ in range(m + 1)] for _ in range(n)]

for i in range(n):  # 주문
    for j in range(1, m + 1):  # 치즈버거 가방
        for l in range(1, k + 1):  # 감자튀김 가방
            if orders[i][0] <= j and orders[i][1] <= l:
                dp[i][j][l] = max(dp[i - 1][j][l], dp[i - 1][j - orders[i][0]][l - orders[i][1]] + 1)
            else:
                dp[i][j][l] = dp[i - 1][j][l]

print(dp[-1][-1][-1])
