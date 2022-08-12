# import sys
# sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T) :
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(N - 1, -1, -1) :
        for j in range(i) :
            if arr[j] < arr[j + 1] :
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    new = [0] * N
    for k in range(N // 2) :
        new[2 * k] = arr[k]
    for k in range(N // 2, N) :
        new[N - 1 - 2 * k] = arr[k]

    print(f'#{t + 1} {" ".join(map(str, new[:10]))}')