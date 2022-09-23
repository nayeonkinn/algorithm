import sys
sys.stdin = open('input/1249.txt')

from collections import deque

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, list(input()))) for _ in range(N)]
    answer = 100 * 100 * 10
    visited = [[100 * 100 * 10] * N for _ in range(N)]
    visited[0][0] = 0
    queue = deque([(0, 0)])

    while queue:
        i, j = queue.popleft()
        for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
            di = i + d[0]
            dj = j + d[1]
            if 0 <= di < N and 0 <= dj < N:
                if visited[i][j] + arr[di][dj] < visited[di][dj]:
                    visited[di][dj] = visited[i][j] + arr[di][dj]
                    queue.append((di, dj))

    print(f'#{t} {visited[N - 1][N - 1]}')


# 아주 느린 DFS

# def dfs(i, j, time):
#     global answer
#     if time > answer:
#         return
#     if i == N - 1 and j == N - 1:
#         answer = min(time, answer)

#     for d in ((-1, 0), (0, 1), (1, 0), (0, -1)):
#         di = i + d[0]
#         dj = j + d[1]
#         if 0 <= di < N and 0 <= dj < N and visited[di][dj] == 0:
#             visited[di][dj] = 1
#             dfs(di, dj, time + arr[di][dj])
#             visited[di][dj] = 0
