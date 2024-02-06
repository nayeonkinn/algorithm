import sys
from collections import deque

sys.stdin = open('input/13460-1.txt')  # 1, 5, 5, -1, 1, 7, -1
input = sys.stdin.readline

def move(di, dj, i, j):
    ni, nj = i + di, j + dj
    while board[ni][nj] != '#':
        if board[ni][nj] == 'O':
            return None, None, True
        ni += di
        nj += dj

    return ni - di, nj - dj, False

n, m = map(int, input().split())
board = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'R':
            ri, rj = i, j
        elif board[i][j] == 'B':
            bi, bj = i, j

q = deque([(ri, rj, bi, bj, 1)])
visited = [(ri, rj, bi, bj)]

while q:
    ri, rj, bi, bj, cnt = q.popleft()

    for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
        nbi, nbj, b_done = move(di, dj, bi, bj)
        if b_done:
            continue

        nri, nrj, r_done = move(di, dj, ri, rj)
        if r_done:
            print(cnt)
            exit()

        if (nri, nrj) == (nbi, nbj):
            if (di, dj) == (-1, 0) and ri < bi or (di, dj) == (1, 0) and ri > bi or \
                (di, dj) == (0, -1) and rj < bj or (di, dj) == (0, 1) and rj > bj:
                nbi -= di
                nbj -= dj
            else:
                nri -= di
                nrj -= dj

        if (nri, nrj, nbi, nbj) not in visited and cnt < 10:
            visited.append((nri, nrj, nbi, nbj))
            q.append((nri, nrj, nbi, nbj, cnt + 1))

print(-1)