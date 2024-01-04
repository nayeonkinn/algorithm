import sys
from bisect import bisect_left
sys.stdin = open('input/11053.txt')  # 4
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

# 1. DP
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))

# 2. Binary Search
bs = []

for i in range(n):
    idx = bisect_left(bs, arr[i])
    if idx < len(bs):
        bs[idx] = arr[i]
    else:
        bs.append(arr[i])

print(len(bs))