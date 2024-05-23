import sys

sys.stdin = open('input/1328-1.txt')  # 2, 1, 18, 0, 4872

def f(i, j, k):
    if 0 in (i, j, k):
        return 0
    
    if dp[i][j][k] != -1:
        return dp[i][j][k]
    
    dp[i][j][k] = (f(i - 1, j - 1, k) + f(i - 1, j, k - 1) + f(i - 1, j, k) * (i - 2)) % 1000000007

    return dp[i][j][k]

N, L, R = map(int, input().split())

dp = [[[-1] * (R + 1) for _ in range(L + 1)] for _ in range(N + 1)]
dp[1][1][1] = 1

print(f(N, L, R))