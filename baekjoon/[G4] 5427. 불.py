import sys
from collections import deque
sys.stdin = open('input/5427.txt') # 2/5/IMPOSSIBLE/IMPOSSIBLE/IMPOSSIBLE

def bfs():
    while True:
        if not sang:
            break

        for _ in range(len(fire)):
            i, j = fire.popleft()
            for d in delta:
                di, dj = i + d[0], j + d[1]
                if 0 <= di < h and 0 <= dj < w and building[di][dj] in ('.', '@'):
                    building[di][dj] = '*'
                    fire.append((di, dj))
        
        for _ in range(len(sang)):
            i, j, time = sang.popleft()
            for d in delta:
                di, dj = i + d[0], j + d[1]
                if not (0 <= di < h and 0 <= dj < w):
                    return time + 1
                elif building[di][dj] == '.' and not visited[di][dj]:
                    visited[di][dj] = True
                    sang.append((di, dj, time + 1))
    
    return 'IMPOSSIBLE'
 
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
t = int(input())
for _ in range(t):
    w, h = map(int, input().split())
    building = [list(input()) for _ in range(h)]
    visited = [[False] * w for _ in range(h)]
    fire = deque([])
    for i in range(h):
        for j in range(w):
            if building[i][j] == '*':
                fire.append((i, j))
            elif building[i][j] == '@':
                sang = deque([(i, j, 0)])
                visited[i][j] = True
    print(bfs())
