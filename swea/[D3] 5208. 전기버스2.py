import sys
sys.stdin = open('input/5208.txt')

def backtracking(idx, battery, cnt):
    global min_cnt
    if battery < 0:
        return
    if cnt >= min_cnt:
        return
    if idx >= N - 1:
        min_cnt = min(cnt, min_cnt)
        return
    backtracking(idx + 1, battery - 1, cnt)
    backtracking(idx + 1, M[idx] - 1, cnt + 1)

T = int(input())
for tc in range(1, T + 1):
    N, *M = list(map(int, input().split()))
    min_cnt = 100
    backtracking(0, 0, -1)
    print(f'#{tc} {min_cnt}')
