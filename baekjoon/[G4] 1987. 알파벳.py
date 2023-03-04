import sys
sys.stdin = open('input/1987-1.txt') # 3, 6, 10
input = sys.stdin.readline

def dfs(i, j, cnt):
    global ans
    ans = max(ans, cnt)

    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < r and 0 <= nj < c and board[ni][nj] not in alpha:
            alpha.add(board[ni][nj])
            dfs(ni, nj, cnt + 1)
            alpha.remove(board[ni][nj])

r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]
alpha = set(board[0][0])
delta = ((-1, 0), (1, 0), (0, -1), (0, 1))

ans = 0
dfs(0, 0, 1)
print(ans)
