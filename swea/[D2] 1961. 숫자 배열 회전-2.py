import sys
sys.stdin = open('input/1961.txt', 'r')

def rotate(arr, N):
    return [''.join([arr[j][i] for j in range(N)[::-1]]) for i in range(N)]

T = int(input())

for t in range(T) :
    N = int(input())
    arr = [input().split() for _ in range(N)]

    arr_90 = rotate(arr, N)
    arr_180 = rotate(arr_90, N)
    arr_270 = rotate(arr_180, N)

    print(f'#{t + 1}')
    for i in range(N):
        print(arr_90[i], end = ' ')
        print(arr_180[i], end = ' ')
        print(arr_270[i])