# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())

for t in range(T) :
    N, M = map(int, input().split())
    flys = [list(map(int, input().split())) for _ in range(N)]

    max = 0
    for i in range(N - M + 1) :
        for j in range(N - M + 1) :
            fly = 0
            for k in range(i, i + M) :
                for l in range(j, j + M) :
                    fly += flys[k][l]
            if fly > max :
                max = fly
    print(f'#{t + 1} {max}')