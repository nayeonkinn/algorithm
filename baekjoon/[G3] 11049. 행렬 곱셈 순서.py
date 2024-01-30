import sys

sys.stdin = open('input/11049.txt')  # 90
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

dp = [[0] * n for _ in range(n)]  # dp[i][j]: i번째 행렬부터 j번째 행렬까지 곱셈 연산의 최솟값

for length in range(1, n):  # 구간 길이 (작은 구간부터 탐색)
    for i in range(n - length):
        j = i + length

        dp[i][j] = 2 ** 31
        for k in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k + 1][j] + arr[i][0] * arr[k][1] * arr[j][1])

print(dp[0][-1])