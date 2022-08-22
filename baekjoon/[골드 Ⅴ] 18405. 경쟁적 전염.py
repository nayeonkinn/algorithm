import sys
sys.stdin = open('input/18405-1.txt', 'r')

N, K = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]
S, X, Y = map(int, input().split())

visited = [[0] * N for _ in range(N)]
delta = ((-1, 0), (0, 1), (1, 0), (0, -1))

virus = []
for i in range(N):
    for j in range(N):
        if board[i][j] != 0:
            virus.append((board[i][j], i, j))
            visited[i][j] = 1

for _ in range(S):
    virus.sort(reverse = True)
    temp = []
    while virus:
        k, i, j = virus.pop()
        for d in range(4):
            di = i + delta[d][0]
            dj = j + delta[d][1]
            if 0 <= di < N and 0 <= dj < N and board[di][dj] == 0:
                board[di][dj] = k
                visited[di][dj] = 1
                temp.append((k, di, dj))
    virus = temp[:]

print(board[X - 1][Y - 1])