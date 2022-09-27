import sys
sys.stdin = open('input/5209.txt')

def backtracking(idx, factory, cost):
    global min_cost
    if idx == N:
        min_cost = min(cost, min_cost)
        return
    if cost >= min_cost:
        return

    for i in range(N):
        if i not in factory:
            backtracking(idx + 1, factory + [i], cost + V[idx][i])

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]
    min_cost = 15 * 15 * 99
    backtracking(0, [], 0)
    print(f'#{tc} {min_cost}')
