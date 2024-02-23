import sys
from copy import deepcopy

sys.stdin = open('input/14939.txt')  # 4
input = sys.stdin.readline

def press(i, j):
    for di, dj in delta:
        ni, nj = i + di, j + dj
        if 0 <= ni < 10 and 0 <= nj < 10:
            new_arr[ni][nj] = not new_arr[ni][nj]

arr = [[False] * 10 for _ in range(10)]

for i in range(10):
    for j, char in enumerate(input().strip()):
        if char == 'O':
            arr[i][j] = True

delta = ((0, 0), (-1, 0), (1, 0), (0, -1), (0, 1))
answer = 1e9

for case in range(1 << 10):
    new_arr = deepcopy(arr)
    cnt = 0

    for num in range(10):
        if case & (1 << num):
            cnt += 1
            press(0, num)
    
    for i in range(1, 10):
        for j in range(10):
            if new_arr[i - 1][j]:
                cnt += 1
                press(i, j)
    
    if not any(new_arr[9]):
        answer = min(answer, cnt)

print(answer if answer != 1e9 else -1)