import sys
sys.stdin = open('input/5186.txt')

T = int(input())
for t in range(1, T + 1):
    f = float(input())
    b = ''
    under, cnt = 1, 0
    while under != 0:
        f *= 2
        over, under = (1, f - 1) if f >= 1 else (0, f)
        b += str(over)
        if over == 1:
            f -= 1
        cnt += 1
        if cnt == 13:
            b = 'overflow'
            break
        
    print(f'#{t} {b}')