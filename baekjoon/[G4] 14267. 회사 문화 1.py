import sys
sys.stdin = open('input/14267.txt') # 0 2 6 6 12


n, m = map(int, input().split())
boss = [0] + list(map(int, input().split()))
dp = [0] * (n + 1)

for _ in range(m):
    num, val = map(int, input().split())
    dp[num] += val

for i in range(2, n + 1):
    dp[i] = dp[boss[i]] + dp[i]

print(*dp[1:])
