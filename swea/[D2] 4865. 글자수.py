import sys
sys.stdin = open('input/4865.txt', 'r')

T = int(input())
for tc in range(T):
    P = list(set(input()))
    T = input()
    D = {}

    for p in P:
        D[p] = T.count(p)

    maxcnt = 0
    for d in D:
        if D[d] > maxcnt:
            maxcnt = D[d]

    print(f'#{tc + 1} {maxcnt}')