# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T) :
    b = [[0] * 10 for _ in range(10)]
    cnt = 0
    N = int(input())
    for n in range(N) :
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2 + 1) :
            for j in range(c1, c2 + 1) :
                b[i][j] += 1
                if b[i][j] == 2 :
                    cnt += 1

    print(f'#{t + 1} {cnt}')