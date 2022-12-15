import sys
sys.stdin = open('input/11123.txt')  # 6 3


import sys
input = sys.stdin.readline

def dfs(i, j):
    queue = [(i, j)]
    visited[i][j] = True
    while queue:
        q = queue.pop(0)
        for d in delta:
            di, dj = q[0] + d[0], q[1] + d[1]
            if 0 <= di < H and 0 <= dj < W and grid[di][dj] == '#' and not visited[di][dj]:
                queue.append((di, dj))
                visited[di][dj] = True

T = int(input())
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))
for tc in range(T):
    H, W = map(int, input().split())
    grid = [input() for _ in range(H)]
    visited = [[False] * W for _ in range(H)]
    answer = 0
    for i in range(H):
        for j in range(W):
            if grid[i][j] == '#' and not visited[i][j]:
                dfs(i, j)
                answer += 1
    print(answer)
