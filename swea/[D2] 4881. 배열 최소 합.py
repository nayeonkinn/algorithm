import sys
sys.stdin = open('input/4881.txt', 'r')

def backtrack(n, N, total):
    global minn
    if n == N:
        if total < minn:
            minn = total
    
    else:
        for i in range(N):
            if i in visited or total > minn:
                continue
            visited[n] = i
            backtrack(n + 1, N, total + arr[n][i])
            visited[n] = -1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    minn = 1000
    visited = [-1] * N
    backtrack(0, N, 0)
    print(f'#{tc} {minn}')