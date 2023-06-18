import sys
from collections import deque
sys.stdin = open('input/3197-1.txt') # 3, 2, 2
input = sys.stdin.readline


def melt():
    while wq:
        i, j = wq.popleft()
        for d in delta:
            di, dj = i + d[0], j + d[1]
            if 0 <= di < r and 0 <= dj < c and not wv[di][dj]:
                wv[di][dj] = True
                if lake[di][dj] == 'X':
                    lake[di][dj] = '.'
                    wq_next.append((di, dj))


def check_swan():
    while sq:
        i, j = sq.popleft()
        if (i, j) == swan[1]:
            return True
        for d in delta:
            di, dj = i + d[0], j + d[1]
            if 0 <= di < r and 0 <= dj < c and not sv[di][dj]:
                sv[di][dj] = True
                if lake[di][dj] == '.':
                    sq.append((di, dj))
                else:
                    sq_next.append((di, dj))
    return False


r, c = map(int, input().split())
lake = [list(input().strip()) for _ in range(r)]
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
sv, sq, sq_next = [[False] * c for _ in range(r)], deque(), deque()
wv, wq, wq_next = [[False] * c for _ in range(r)], deque(), deque()

swan = []
for i in range(r):
    for j in range(c):
        if lake[i][j] == 'L':
            swan.append((i, j))
            lake[i][j] = '.'
            wq.append((i, j))
        elif lake[i][j] == '.':
            wq.append((i, j))
sq.append(swan[0])

day = 0
while True:
    day += 1
    melt()
    if check_swan():
        print(day)
        break
    sq, wq = sq_next, wq_next
    sq_next, wq_next = deque(), deque()
