from collections import deque
import sys

sys.stdin = open('input/2842-3.txt')  # 0, 2, 5
input = sys.stdin.readline

def bfs(i, j):
    q = deque([(i, j)])
    visited = [[False] * N for _ in range(N)]
    visited[i][j] = True

    cnt = 0

    while q:
        i, j = q.popleft()

        if town[i][j] == 'K':
            cnt += 1
        if cnt == houses:
            break

        for di, dj in ((-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
            ni, nj = di + i, dj + j

            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and fatigue[left] <= altitude[ni][nj] <= fatigue[right]:
                visited[ni][nj] = True
                q.append((ni, nj))
    
    return cnt

N = int(input())
town = [input().strip() for _ in range(N)]
altitude = [list(map(int, input().split())) for _ in range(N)]

answer = 1e9
houses = 0

for i in range(N):
    for j in range(N):
        if town[i][j] == 'P':
            pi, pj = i, j
        elif town[i][j] == 'K':
            houses += 1

fatigue = sorted(set(sum(altitude, [])))
left, right = 0, 0

while left <= right < len(fatigue):
    cnt = 0

    if fatigue[left] <= altitude[pi][pj] <= fatigue[right]:
        cnt = bfs(pi, pj)

    if cnt == houses:
        answer = min(answer, fatigue[right] - fatigue[left])
        left += 1
    else:
        right += 1

print(answer)