# import sys
# sys.stdin = open('input.txt', 'r')

def binary(P, N) :
    cnt = 0
    l, r = 1, P
    while True :
        c = int((l + r) / 2)
        cnt += 1
        if c == N :
            return cnt
        elif c < N :
            l = c
        else :
            r = c

T = int(input())
for t in range(T) :
    P, Pa, Pb = map(int, input().split())
    A, B = binary(P, Pa), binary(P, Pb)
    if A < B :
        result = 'A'
    elif A > B :
        result = 'B'
    else :
        result = 0
    print(f'#{t + 1} {result}')