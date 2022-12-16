import sys
sys.stdin = open('input/14501-1.txt') # 45, 55, 20, 90


import sys
input = sys.stdin.readline

# dfs
def dfs(idx, profit):
    global answer

    if idx == n:
        answer = max(profit, answer)
        return
    elif idx > n:
        return
    
    dfs(idx + info[idx][0], profit + info[idx][1])
    dfs(idx + 1, profit)

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
answer = 0
dfs(0, 0)
print(answer)


# dp
# n = int(input())
# time, profit = zip(*[list(map(int, input().split())) for _ in range(n)])
# dp = [0] * (n + 1)

# for i in range(n - 1, -1, -1):
#     if time[i] + i <= n:
#         dp[i] = max(dp[i + time[i]] + profit[i], dp[i + 1])
#     else:
#         dp[i] = dp[i + 1]

# print(dp[0])
