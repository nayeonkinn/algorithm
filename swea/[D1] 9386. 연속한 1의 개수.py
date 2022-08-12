from multiprocessing import context
# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T) :
    N = int(input())
    arr = input()
    maxcnt = cnt = 0
    for a in arr :
        if a == '1' :
            cnt += 1
            if cnt > maxcnt :
                maxcnt = cnt
        else :
            cnt = 0
    print(f'#{t + 1} {maxcnt}')