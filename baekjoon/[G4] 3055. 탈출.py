import sys
sys.stdin = open('input/3055-1.txt') # 3, KAKTUS, 6, 4

from collections import deque

def bfs():
    global answer
    if not water and not queue:
        answer = 'KAKTUS'
        return

    for _ in range(len(water)):
        i, j = water.popleft()
        for d in delta:
            di = i + d[0]
            dj = j + d[1]
            if 0 <= di < R and 0 <= dj < C and forest[di][dj] in '.S':
                forest[di][dj] = '*'
                water.append((di, dj))
    
    for _ in range(len(queue)):
        i, j = queue.popleft()
        if (i, j) == D:
            answer = visited[i][j] - 1
            return
        for d in delta:
            di = i + d[0]
            dj = j + d[1]
            if 0 <= di < R and 0 <= dj < C and forest[di][dj] in '.D' and visited[di][dj] == 0:
                visited[di][dj] = visited[i][j] + 1
                forest[di][dj] = 'S'
                queue.append((di, dj))

    bfs()

R, C = map(int, input().split())
forest = [list(input()) for _ in range(R)]
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
water = deque()
visited = [[0] * C for _ in range(R)]
for i in range(R):
    for j in range(C):
        if forest[i][j] == 'D':
            D = (i, j)
        elif forest[i][j] == 'S':
            queue = deque([(i, j)])
            visited[i][j] = 1
        elif forest[i][j] == '*':
            water.append((i, j))

bfs()
print(answer)