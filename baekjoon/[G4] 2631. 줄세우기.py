import sys

sys.stdin = open('input/2631.txt')  # 4

n = int(input())
kids = [int(input()) for _ in range(n)]

dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if kids[j] < kids[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))