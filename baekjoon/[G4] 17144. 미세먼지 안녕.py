import sys

sys.stdin = open('input/17144-1.txt')  # 188, 188, 186, 178, 172, 71, 52, 46
input = sys.stdin.readline

def spread():
    new_arr = [[0] * C for _ in range(R)]
    new_arr[pi][0] = new_arr[pi + 1][0] = -1
    
    for i in range(R):
        for j in range(C):
            if arr[i][j] > 0:
                cnt = 0

                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj

                    if 0 <= ni < R and 0 <= nj < C and (ni, nj) not in ((pi, 0), (pi + 1, 0)):
                        cnt += 1
                        new_arr[ni][nj] += arr[i][j] // 5
                
                new_arr[i][j] += arr[i][j] - cnt * (arr[i][j] // 5)

    return new_arr

def purify():
    for i in range(pi - 1, 0, -1):
        arr[i][0] = arr[i - 1][0]
    for i in range(pi + 2, R - 1):
        arr[i][0] = arr[i + 1][0]

    for j in range(C - 1):
        arr[0][j] = arr[0][j + 1]
        arr[-1][j] = arr[-1][j + 1]

    for i in range(pi):
        arr[i][-1] = arr[i + 1][-1]
    for i in range(R - 1, pi + 1, -1):
        arr[i][-1] = arr[i - 1][-1]

    for j in range(C - 1, 1, -1):
        arr[pi][j] = arr[pi][j - 1]
        arr[pi + 1][j] = arr[pi + 1][j - 1]

    arr[pi][1] = arr[pi + 1][1] = 0

R, C, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]

for i in range(R):
    if arr[i][0] == -1:
        pi = i
        break

for _ in range(T):
    arr = spread()
    purify()

print(sum(map(sum, arr)) + 2)