import sys
sys.stdin = open('input/12865.txt') # 14
input = sys.stdin.readline

n, k = map(int, input().split())
weight, value = zip(*[list(map(int, input().split())) for _ in range(n)])
dp = [[0] * (k + 1) for _ in range(n + 1)]
print(n, k, weight, value)

for i in range(1, n + 1):
    for j in range(1, k + 1):
        if weight[i - 1] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight[i - 1]] + value[i - 1])
    print(dp)

print(dp[-1][-1])
