import sys

sys.stdin = open('input/15989.txt') # 4  8  14
input = sys.stdin.readline

t = int(input())
nums = [int(input()) for _ in range(t)]

max_n = max(nums) + 1
dp = [1] * max_n

for i in range(2, max_n):
    dp[i] += dp[i - 2]

for i in range(3, max_n):
    dp[i] += dp[i - 3]

for n in nums:
    print(dp[n])