import sys
sys.stdin = open('input/2005.txt')

def paskal(a, b):
    if (a, b) in d:
        return d[a, b]
    
    if b == 0 or a == b:
        d[a, b] = 1
        return d[a, b]
    else:
        d[a, b] = paskal(a - 1, b - 1) + paskal(a - 1, b)
        return d[a, b]

d = {}
T = int(input())
for tc in range(T):
    print(f'#{tc + 1}')
    N = int(input())
    for i in range(N):
        for j in range(i + 1):
            print(paskal(i, j), end = ' ')
        print()