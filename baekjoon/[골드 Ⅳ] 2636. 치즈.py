import sys
sys.stdin = open('input/2636.txt', 'r')  # 3, 5

r, c = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(r)]

q = [(0, 0), (0, c - 1), (r - 1, 0), (r - 1, c -1)]
visited = [[0] * c for _ in range(r)]
time = 0
cheese = []

while True:
    while q:
        v = q.pop(0)
        board[v[0]][v[1]] = -1
        visited[v[0]][v[1]] = 1
        for d in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            di = v[0] + d[0]
            dj = v[1] + d[1]
            if 0 <= di < r and 0 <= dj < c and visited[di][dj] == 0:
                visited[di][dj] = 1
                if board[di][dj] == 0:
                    q.append((di, dj))
                elif board[di][dj] == 1:
                    cheese.append((di, dj))
                    board[di][dj] == 0

    if cheese:
        time += 1
        cheese_cnt = len(cheese)
        q = cheese[:]
        cheese = []
    else:
        break

print(time)
print(cheese_cnt)