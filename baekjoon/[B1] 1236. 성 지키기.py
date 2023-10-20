import sys
sys.stdin = open('input/1236-3.txt')  # 4, 0, 3


N, M = map(int, input().split())
castle = [input() for _ in range(N)]

row, col = 0, 0

for i in range(N):
    if 'X' not in castle[i]:
        row += 1

for j in range(M):
    if 'X' not in [castle[i][j] for i in range(N)]:
        col += 1

print(max(row, col))
