import sys
sys.stdin = open('input/7579.txt')  # 6, 1

n, m = map(int, input().split())
memory = list(map(int, input().split()))
cost = list(map(int, input().split()))

answer = 1e9
dp = [[0] * (sum(cost) + 1) for _ in range(n)]  # dp[i][j]: i번째 앱까지 확인했을 때, j 비용으로 사용할 수 있는 최대의 메모리

for i in range(n):
    for j in range(sum(cost) + 1):  # 0원인 경우도 고려해야 함
        if cost[i] > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - cost[i]] + memory[i])

        if dp[i][j] >= m and j < answer:
            answer = min(answer, j)

print(answer)