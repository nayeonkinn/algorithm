import sys

sys.stdin = open('input/16724.txt')  # 2
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [input().strip() for _ in range(n)]

d = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

zone = [[None] * m for _ in range(n)]

idx = 0
dup = 0

for i in range(n):
    for j in range(m):
        if not zone[i][j]:
            idx += 1

            x, y = i, j
            while not zone[x][y]:
                zone[x][y] = idx

                dx, dy = d[arr[x][y]]
                x, y = x + dx, y + dy

            if zone[x][y] != idx:
                dup += 1

print(idx - dup)