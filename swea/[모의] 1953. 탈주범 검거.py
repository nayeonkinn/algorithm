import sys
sys.stdin = open('input/1953.txt')

from collections import deque

pipe = [[], [(-1, 0), (0, 1), (1, 0), (0, -1)], [(-1, 0), (1, 0)], [(0, 1), (0, -1)], [(-1, 0), (0, 1)], [(0, 1), (1, 0)], [(1, 0), (0, -1)], [(-1, 0), (0, -1)]]

T = int(input())
for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    under = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]
    visited[R][C] = 1
    q = deque([(R, C)])
    cnt = 1

    while q:
        i, j = q.popleft()
        if visited[i][j] == L:
            break
        for d in pipe[under[i][j]]:
            di = i + d[0]
            dj = j + d[1]
            if 0 <= di < N and 0 <= dj < M and visited[di][dj] == 0 and (-d[0], -d[1]) in pipe[under[di][dj]]:
                visited[di][dj] = visited[i][j] + 1
                q.append((di, dj))
                cnt += 1

    print(f'#{t} {cnt}')
