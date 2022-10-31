import sys
sys.stdin = open('input/19236-1.txt') # 33, 43, 76, 39

import copy

def find_fish(x, info):
    for i in range(4):
        for j in range(4):
            if info[i][j][0] == x:
                return i, j
    return -1, -1

def bfs(x, y, info, total):
    global answer
    total += info[x][y][0] + 1
    direction = info[x][y][1]
    info[x][y] = [-1, -1]
    
    for i in range(16):
        fx, fy = find_fish(i, info)
        if (fx, fy) == (-1, -1):
            continue

        for _ in range(8):
            dx, dy = fx + delta[info[fx][fy][1]][0], fy + delta[info[fx][fy][1]][1]
            if not (0 <= dx < 4 and 0 <= dy < 4) or (dx == x and dy == y):
                info[fx][fy][1] = (info[fx][fy][1] + 1) % 8
                continue
            info[fx][fy], info[dx][dy] = info[dx][dy], info[fx][fy]
            break

    for j in range(1, 4):
        move = False
        ni, nj = x + delta[direction][0] * j, y + delta[direction][1] * j
        if 0 <= ni < 4 and 0 <= nj < 4 and info[ni][nj][0] != -1:
            bfs(ni, nj, copy.deepcopy(info), total)
            move = True
    if not move:
        answer = max(total, answer)


info = [[0] * 4 for _ in range(4)]
for i in range(4):
    temp = list(map(int, input().split()))
    for j in range(4):
        info[i][j] = [temp[2 * j] - 1, temp[2 * j + 1] - 1]

delta = ((-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1))
answer = 0
bfs(0, 0, info, 0)
print(answer)