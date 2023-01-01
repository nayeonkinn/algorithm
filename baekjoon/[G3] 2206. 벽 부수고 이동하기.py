import sys
from collections import deque
sys.stdin = open('input/2206-1.txt') # 15, -1
input = sys.stdin.readline

def bfs():
    delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
    queue = deque([(0, 0, 1, False)])
    visited = [[[False] * 2 for _ in range(m)] for _ in range(n)]
    visited[0][0][0] = True

    while queue:
        i, j, cnt, flag = queue.popleft()
        if i == n - 1 and j == m - 1:
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
maze = [list(map(int, list(input().strip()))) for _ in range(n)]
print(bfs())
