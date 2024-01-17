import sys

sys.stdin = open('input/10942.txt')  # 1  0  1  1
input = sys.stdin.readline

n = int(input())
nums = [0] + list(map(int, input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    dp[i][i] = 1

for i in range(1, n):
    if nums[i] == nums[i + 1]:
        dp[i][i + 1] = 1

for i in range(n - 2, 0, -1):
    for j in range(i + 2, n + 1):
        if nums[i] == nums[j] and dp[i + 1][j - 1]:
            dp[i][j] = 1

m = int(input())
for _ in range(m):
    s, e = map(int, input().split())
    print(dp[s][e])