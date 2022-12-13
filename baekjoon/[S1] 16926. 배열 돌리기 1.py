import sys
sys.stdin = open('input/16926-1.txt')

# pypy로만 가능
N, M, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

for _ in range(R):
    for i in range(min(N, M) // 2):
        x, y = i, i
        temp = arr[x][y]

        for j in range(i + 1, N - i):
            x = j
            arr[x][y], temp = temp, arr[x][y]
        
        for j in range(i + 1, M - i):
            y = j
            arr[x][y], temp = temp, arr[x][y]

        for j in range(i + 1, N - i):
            x = N - 1 - j
            arr[x][y], temp = temp, arr[x][y]

        for j in range(i + 1, M - i):
            y = M - 1 - j
            arr[x][y], temp = temp, arr[x][y]

for i in range(N):
    print(*arr[i])