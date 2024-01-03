import sys
sys.stdin = open('input/2096-1.txt')  # 18 6, 0 0
input = sys.stdin.readline

n = int(input())

dp = list(map(int, input().split()))
dp = [dp, dp]  # [최대 점수, 최소 점수]
f = max, min  # 최대 점수 계산 시엔 max 함수, 최소 점수 계산 시엔 min 함수 사용

for _ in range(n - 1):
    a, b, c = map(int, input().split())
    for i in range(2):
        dp[i] = [f[i](dp[i][:2]) + a, f[i](dp[i]) + b, f[i](dp[i][1:]) + c]

print(max(dp[0]), min(dp[1]))