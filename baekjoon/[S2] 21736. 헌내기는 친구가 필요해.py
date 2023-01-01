import sys
from collections import deque
sys.stdin = open('input/21736-1.txt')  # 1, TT
input = sys.stdin.readline

n, m = map(int, input().split())
delta = ((0, -1), (0, 1), (1, 0), (-1, 0))
campus = []
for i in range(n):
    campus.append(list(input()))
    for j in range(m):
        if campus[i][j] == 'I':
            campus[i][j] = 'X'
            queue = deque([(i, j)])

cnt = 0
while queue:
    i, j = queue.popleft()
    for di, dj in delta:
        ni, nj = di + i, dj + j
        if 0 <= ni < n and 0 <= nj < m and campus[ni][nj] != 'X':
            if campus[ni][nj] == 'P':
                cnt += 1
            campus[ni][nj] = 'X'
            queue.append((ni, nj))

print(cnt) if cnt else print('TT')
