import sys
sys.stdin = open('input/1799.txt')

import copy

def is_promising(i, j, bishop):
    for bi, bj in bishop:
        if abs(i - bi) == abs(j - bj):
            return False
    return True

def add(i, j, chess):
    # print(i, j)
    # for k in range(n):
    #     print(chess[k])
    for k in range(n):
        di, dj, dj2 = i + k, j + k, j - k
        if 0 <= di < n and 0 <= dj < n:
            chess[di][dj] = 0
        if 0 <= di < n and 0 <= dj2 < n:
            chess[di][dj2] = 0
    # print()
    # for k in range(n):
    #     print(chess[k])
    # print()
    return chess

def backtracking(idx, bishop, chess):
    global answer
    if idx == n ** 2 - 1:
        answer = max(len(bishop), answer)
        return

    for x in range(idx + 1, n ** 2):
        i, j = x // n, x % n
        if not chess[i][j]:
            continue
        if is_promising(i, j, bishop):
            backtracking(x, bishop + [(i, j)], add(i, j, copy.deepcopy(chess)))
        else:
            backtracking(x, bishop, chess)

n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
answer = 0
backtracking(0, [], chess)
print(answer)
