import sys

sys.stdin = open('input/2169.txt')  # 319
input = sys.stdin.readline

n, m = map(int, input().split())
dp = [list(map(int, input().split())) for _ in range(n)]
# 각 칸으로 올 수 있는 세 방법에 대해 비교 (위, 왼쪽, 오른쪽)

# 첫번째 행은 오른쪽으로 이동하는 방법뿐
for j in range(1, m):
    dp[0][j] += dp[0][j - 1]

# 나머지 행에 대해 오른쪽으로 이동하는 경우, 왼쪽으로 이동하는 경우 계산 후 최대값 저장
for i in range(1, n):
    right = dp[i][:]
    right[0] += dp[i - 1][0]  # 첫번째 열은 위에서 오는 경우뿐
    for j in range(1, m):
        right[j] += max(dp[i - 1][j], right[j - 1])  # 위에서 오는 경우와 왼쪽에서 오는 경우 비교

    left = dp[i][:]
    left[m - 1] += dp[i - 1][m - 1]  # 마지막 열은 위에서 오는 경우뿐
    for j in range(m - 2, -1, -1):
        left[j] += max(dp[i - 1][j], left[j + 1])  # 위에서 오는 경우와 오른쪽에서 오는 경우 비교
    
    for j in range(m):
        dp[i][j] = max(right[j], left[j])  # 두 방법 중 최대값 계산

print(dp[-1][-1])