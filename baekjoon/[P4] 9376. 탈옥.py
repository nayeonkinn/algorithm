from collections import deque
import sys

sys.stdin = open('input/9376.txt')  # 4  0  9
input = sys.stdin.readline

for _ in range(int(input())):
    h, w = map(int, input().split())
    jail = ['.' * (w + 2)] + ['.' + input().strip() + '.' for _ in range(h)] + ['.' * (w + 2)]

    costs = [[[10000] * 3 for _ in range(w + 2)] for _ in range(h + 2)]
    inmate = [(0, 0)] + [(i, j) for i in range(h + 2) for j in range(w + 2) if jail[i][j] == '$']

    for idx in range(3):
        q = deque([(inmate[idx][0], inmate[idx][1])])
        costs[inmate[idx][0]][inmate[idx][1]][idx] = 0

        while q:
            i, j = q.popleft()

            for ni, nj in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if 0 <= ni < h + 2 and 0 <= nj < w + 2 and jail[ni][nj] != '*' and costs[ni][nj][idx] == 10000:
                    if jail[ni][nj] == '#':
                        costs[ni][nj][idx] = costs[i][j][idx] + 1
                        q.append((ni, nj))
                    else:
                        costs[ni][nj][idx] = costs[i][j][idx]
                        q.appendleft((ni, nj))

    for i in range(h + 2):
        for j in range(w + 2):
            costs[i][j] = sum(costs[i][j]) - 2 if jail[i][j] == '#' else sum(costs[i][j])
    print(min(map(min, costs)))