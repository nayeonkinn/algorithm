import sys

sys.stdin = open('input/2342.txt')  # 8

def power(x, y):
    if x == y:
        return 1
    elif x == 0:
        return 2
    elif abs(x - y) == 1 or abs(x - y) == 3:
        return 3
    else:  # elif abs(x - y) == 2:
        return 4
    
arr = list(map(int, input().split()))
n = len(arr) - 1

dp = [[[1e9] * 5 for _ in range(5)] for _ in range(n + 1)]  # dp[i][j][k]: i번째 이동 시 왼발은 j, 오른발은 k에 있을 경우의 최소 힘
dp[0][0][0] = 0

for i in range(n):  # i번째 이동
    move = arr[i]  # i번째 이동의 위치
    for j in range(5):  # 이동하지 않는 발의 모든 위치
        for before in range(5):  # 이동하는 발의 모든 이전 위치
            p = power(before, move)
            dp[i + 1][move][j] = min(dp[i + 1][move][j], dp[i][before][j] + p)  # 왼발 이동
            dp[i + 1][j][move] = min(dp[i + 1][j][move], dp[i][j][before] + p)  # 오른발 이동

print(min(map(min, dp[n])))