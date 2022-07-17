T = int(input())

for t in range(T) :
    N, M = map(int, input().split())
    array = []
    for n in range(N) :
        array.append(list(map(int, input().split())))

    max = 0
    for i in range(N - M + 1) :
        for j in range(N - M + 1) :
            fly = 0
            for k in range(M) :
                for l in range(M) :
                    fly += array[i + k][j + l]
            if fly > max :
                max = fly
    print("#%d %d" % (t + 1, max))