import sys
sys.stdin = open('input/17141-7.txt') # (17141과 동일) 4, 4, 4, 3, 7, -1, 0

import itertools

def laboratory():
    total_virus = 0
    start = []
    for i in range(N):
        for j in range(N):
            if lab[i][j] == 2:
                start.append((i, j))
            if lab[i][j] == 0:
                total_virus += 1
    if total_virus == 0:
        return 0

    combi = list(itertools.combinations(start, M))
    min_time = N * N
    for com in combi:
        virus = 0
        q, visited = [], [[-1] * N for _ in range(N)]
        for c in com:
            q.append((c[0], c[1]))
            visited[c[0]][c[1]] = 0

        while q:
            v = q.pop(0)
            for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                di, dj = v[0] + d[0], v[1] + d[1]
                if 0 <= di < N and 0 <= dj < N and lab[di][dj] != 1 and visited[di][dj] == -1:
                    visited[di][dj] = visited[v[0]][v[1]] + 1
                    if lab[di][dj] != 2:
                        virus += 1
                    if virus == total_virus:
                        min_time = min(min_time, visited[di][dj])
                        break
                    q.append((di, dj))
    if min_time == N * N:
        min_time = -1

    return min_time

N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
print(laboratory())