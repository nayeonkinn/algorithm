import sys
sys.stdin = open('input.txt', 'r')

def max(a, b) :
    return a if a > b else b

for t in range(10) :
    input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    maxx = 0
    for i in range(100) :
        rsum = csum = rdsum = ldsum = 0
        for j in range(100) :
            rsum += arr[i][j]
            csum += arr[j][i]
        maxx = max(rsum, maxx)
        maxx = max(csum, maxx)
        rdsum += arr[i][i]
        ldsum += arr[i][99 - i]
    maxx = max(rdsum, maxx)
    maxx = max(ldsum, maxx)
    print(f'#{t + 1} {maxx}')