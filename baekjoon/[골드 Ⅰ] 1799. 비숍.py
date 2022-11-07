import sys
sys.stdin = open('input/1799.txt')

def is_promising(candidate, bishop):
    i, j = candidate
    for bi, bj in bishop:
        if abs(i - bi) == abs(j - bj):
            return False
    return True

def backtracking(idx, bishop, type):
    global answer
    if idx == len(candidates) - 1:
        if type:
            odd = max(len(bishop), odd)
        else:
            even = max(len(bishop), even)
        return

    for i in range(idx + 1, len(candidates)):
        if is_promising(candidates[i], bishop):
            backtracking(i, bishop + [candidates[i]], type)
        else:
            backtracking(i, bishop, type)

n = int(input())
chess = [list(map(int, input().split())) for _ in range(n)]
candidates = [(i, j) for i in range(n) for j in range(n) if chess[i][j]]
even, odd = 0, 0
backtracking(0, [], 0)
backtracking(0, [], 1)
print(even + odd)
