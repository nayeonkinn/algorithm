import sys
sys.stdin = open('input/4012.txt')

def taste(lst):
    result = 0
    for i in range(N // 2 - 1):
        for j in range(i + 1, N // 2):
            x, y = lst[i], lst[j]
            result += synergy[x][y] + synergy[y][x]
    return result

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    synergy = [list(map(int, input().split())) for _ in range(N)]
    min_diff = 20000

    for i in range(1 << N):
        A, B, cnt = [], [], 0
        for j in range(N):
            if i & (1 << j):
                cnt += 1
                A.append(j)
            else:
                B.append(j)
        if cnt == N // 2:
            diff = abs(taste(A) - taste(B))
            min_diff = min(diff, min_diff)

    print(f'#{t} {min_diff}')
