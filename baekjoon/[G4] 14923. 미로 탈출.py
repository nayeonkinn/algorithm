import sys
from collections import deque
sys.stdin = open('input/14923.txt') # 11
input = sys.stdin.readline

def bfs():
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
    queue = deque([(hi, hj, 0, False)])
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[hi][hj][0] = True

    while queue:
        i, j, cnt, flag = queue.popleft()
        if i == ei and j == ej:
            return cnt

        for di, dj in delta:
            ni, nj = di + i, dj + j
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj][flag]:
                visited[ni][nj][flag] = True
                if maze[ni][nj] == 0:
                    queue.append((ni, nj, cnt + 1, flag))
                elif maze[ni][nj] == 1 and not flag:
                    queue.append((ni, nj, cnt + 1, True))
    
    return -1

n, m = map(int, input().split())
hi, hj = map(lambda x: int(x) - 1, input().split())
ei, ej = map(lambda x: int(x) - 1, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
print(bfs())
