import sys
sys.stdin = open('input/19238-1.txt') # 14, -1, -1, 57, 20, -1, 4, 5000

from collections import deque

def taxi(i, j):
    global fuel, cnt

    queue = deque([(i, j)])
    visited = [[0] * N for _ in range(N)]
    visited[i][j] = 1

    candidate = []
    if arr[i][j] > 1:
        candidate.append((i, j, arr[i][j], visited[i][j] - 1))
    while not candidate:
        if not queue:
            return -1
        for _ in range(len(queue)):
            i, j = queue.popleft()
            if arr[i][j] > 1:
                candidate.append((i, j, arr[i][j], visited[i][j] - 1))

            for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                di += i
                dj += j
                if 0 <= di < N and 0 <= dj < N and arr[di][dj] != 1 and visited[di][dj] == 0:
                    visited[di][dj] = visited[i][j] + 1
                    queue.append((di, dj))

    pi, pj, pnum, pfuel = sorted(candidate)[0]
    arr[pi][pj] = 0
    fuel -= pfuel
    if fuel < 0:
        return -1

    queue = deque([(pi, pj)])
    visited = [[0] * N for _ in range(N)]
    visited[pi][pj] = 1

    flag = False
    while queue:
        i, j = queue.popleft()
        if (i, j) == passengers[pnum]:
            flag = True
            break

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            di += i
            dj += j
            if 0 <= di < N and 0 <= dj < N and arr[di][dj] != 1 and visited[di][dj] == 0:
                visited[di][dj] = visited[i][j] + 1
                queue.append((di, dj))

    if not flag or fuel < visited[i][j] - 1:
        return -1
    fuel += visited[i][j] - 1
    cnt += 1

    if cnt == M:
        return fuel
    else:
        return taxi(i, j)


N, M, fuel = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
di, dj = map(lambda x: int(x) - 1, input().split())
passengers = {}
for i in range(2, M + 2):
    si, sj, ei, ej = map(lambda x: int(x) - 1, input().split())
    arr[si][sj] = i
    passengers[i] = (ei, ej)
cnt = 0
print(taxi(di, dj))
