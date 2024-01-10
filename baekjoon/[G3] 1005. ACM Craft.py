import sys
from collections import deque

sys.stdin = open('input/1005-1.txt')  # 120  39, 6  5  399990  2  0
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    time = [0] + list(map(int, input().split()))
    edges = [[] for _ in range(n + 1)]
    indegree = [0] * (n + 1)
    dp = [0] * (n + 1)
    q = deque()

    for _ in range(k):
        x, y = map(int, input().split())
        edges[x].append(y)
        indegree[y] += 1

    for i in range(1, n + 1):
        if not indegree[i]:
            q.append(i)
            dp[i] = time[i]

    while q:
        x = q.popleft()

        for y in edges[x]:
            indegree[y] -= 1
            dp[y] = max(dp[x] + time[y] , dp[y])

            if not indegree[y]:
                q.append(y)

    print(dp[int(input())])