# import sys
# sys.stdin = open('input.txt')

T = int(input())
for t in range(T) :
    N, M = map(int, input().split())
    pic = [list(map(int, input().split())) for _ in range(N)]

    maxcnt = 0
    for i in range(N) :
        cnt = 0
        for j in range(M) :
            if pic[i][j] == 1 :
                cnt += 1
                if cnt > maxcnt :
                    maxcnt = cnt
            else :
                cnt = 0

    for j in range(M) :
        cnt = 0
        for i in range(N) :
            if pic[i][j] == 1 :
                cnt += 1
                if cnt > maxcnt :
                    maxcnt = cnt
            else :
                cnt = 0

    print(f'#{t + 1} {maxcnt}')