import sys
sys.stdin = open('input/2806.txt')

def promising(queens, idx, num):
    if num in queens:
        return 0
    for i in range(idx):
        if abs(i - idx) == abs(queens[i] - num):
            return 0
    return 1

def backtracking(idx, queens):
    global cnt
    if idx == N:
        cnt += 1
        return
    
    for i in range(N):
        if promising(queens, idx, i):
            backtracking(idx + 1, queens + [i])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    backtracking(0, [])
    print(f'#{tc} {cnt}')
