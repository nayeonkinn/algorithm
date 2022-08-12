import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T) :
    N, M = input().split()
    numbers = [int(n) for n in input().split()]

    maxx = 0
    minn = 1000000
    for i in range(int(N) - int(M) + 1) :
        summ = 0
        for j in range(int(M)) :
            summ += numbers[i + j]
        if summ > maxx :
            maxx = summ
        if summ < minn :
            minn = summ
            
    print(f'#{t + 1} {maxx - minn}')