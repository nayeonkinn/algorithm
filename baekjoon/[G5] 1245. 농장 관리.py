import sys
sys.stdin = open('input/1245.txt') # 3


import sys
from collections import deque


def check(i, j):
    global peak
    
    queue = deque([(i, j)])
    visited[i][j] = True
    flag = True

    while queue:
        i, j = queue.popleft()
        
        for d in delta:
            di, dj = d[0] + i, d[1] + j
            if 0 <= di < n and 0 <= dj < m:
                if farm[di][dj] > farm[i][j]:
                    flag = False
                if not visited[di][dj] and farm[di][dj] == farm[i][j]:
                    visited[di][dj] = True
                    queue.append((di, dj))

    if flag:
        peak += 1


input = sys.stdin.readline
n, m = map(int, input().split())
farm = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]
delta = [(i, j) for i in range(-1, 2) for j in range(-1, 2)]

peak = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
           check(i, j)

print(peak)
