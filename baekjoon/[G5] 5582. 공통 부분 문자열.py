import sys
sys.stdin = open('input/5582-1.txt')  # 5, 0

a = input()
b = input()

dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]

for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1] + 1

print(max(map(max, dp)))
