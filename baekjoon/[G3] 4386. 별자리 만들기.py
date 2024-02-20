import heapq, sys

sys.stdin = open('input/4386.txt')  # 3.41
input = sys.stdin.readline

n = int(input())
stars = [list(map(float, input().split())) for _ in range(n)]

costs = [[0] * n for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        cost = round(((stars[i][0] - stars[j][0]) ** 2 + (stars[i][1] - stars[j][1]) ** 2) ** 0.5, 2)
        costs[i][j] = cost
        costs[j][i] = cost
    
hq = []
heapq.heappush(hq, (0, 0))

visited = [False] * n

answer = 0

while hq:
    cost, now = heapq.heappop(hq)

    if not visited[now]:
        visited[now] = True
        answer += cost

        for nxt in range(n):
            if not visited[nxt] and now != nxt:
                heapq.heappush(hq, (costs[now][nxt], nxt))

print(answer)