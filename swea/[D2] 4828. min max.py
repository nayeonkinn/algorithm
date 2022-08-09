import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T) :
    N = int(input())
    num = [int(a) for a in input().split()]
    
    minn = num[0]
    maxx = num[0]

    for a in num :
        if a < minn :
            minn = a
        if a > maxx :
            maxx = a

    print(f'#{t + 1} {maxx - minn}')