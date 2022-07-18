T = int(input())

for t in range(T) :
    N = int(input())
    array = []
    for n in range(N) :
        array.append(list(map(int, input().split())))

    print(f'#{t + 1}')
    for i in range(N) :
        for j in range(N)[::-1] :
            print(array[j][i], end = '')
        print(' ', end = '')
        for k in range(N)[::-1] :
            print(array[N - i - 1][k], end = '')
        print(' ', end = '')
        for l in range(N) :
            print(array[l][N - i - 1], end = '')
        print(' ')