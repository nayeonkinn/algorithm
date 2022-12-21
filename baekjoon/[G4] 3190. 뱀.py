import sys
sys.stdin = open('input/3190-1.txt') # 9, 21, 13
input = sys.stdin.readline

n, k = int(input()), int(input())
board = [[0] * n for _ in range(n)]
for _ in range(k):
    i, j = map(int, input().split())
    board[i - 1][j - 1] = 1
board[0][0] = 2

l = int(input())
info = {}
for _ in range(l):
    x, c = map(lambda x: int(x) if x.isdigit() else x, input().split())
    info[x + 1] = c
delta, d = ((0, 1), (1, 0), (0, -1), (-1, 0)), 0

time, i, j = 0, 0, 0
snake = [(0, 0)]
while True:
    time += 1
    if info.get(time) == 'L':
        d = (d - 1) % 4
    elif info.get(time) == 'D':
        d = (d + 1) % 4
    di, dj = i + delta[d][0], j + delta[d][1]

    if not (0 <= di < n and 0 <= dj < n) or board[di][dj] == 2:
        break
    
    if board[di][dj] == 0:
        tail = snake.pop(0)
        board[tail[0]][tail[1]] = 0
    board[di][dj] = 2
    snake.append((di, dj))
    i, j = di, dj

print(time)