from collections import deque
import sys

sys.stdin = open('input/4179.txt')  # 3, IMPOSSIBLE
input = sys.stdin.readline

def bfs(arr, flag):
    for _ in range(len(arr)):
        i, j, cnt = arr.popleft()

        if flag == 'J' and (i in (0, r - 1) or j in (0, c - 1)):
            print(cnt)
            exit()

        for di, dj in delta:
            ni, nj = i + di, j + dj

            if 0 <= ni < r and 0 <= nj < c and maze[ni][nj] == '.':
                maze[ni][nj] = flag
                arr.append((ni, nj, cnt + 1))

    return arr

r, c = map(int, input().split())
maze = [list(input().strip()) for _ in range(r)]

jh = deque([])
fire = deque([])

delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

for i in range(r):
    for j in range(c):
        if maze[i][j] == 'J':
            jh.append((i, j, 1))
        elif maze[i][j] == 'F':
            fire.append((i, j, 1))

while jh:
    fire = bfs(fire, 'F')
    jh = bfs(jh, 'J')

print('IMPOSSIBLE')