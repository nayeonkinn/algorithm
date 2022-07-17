T = int(input())
for t in range(T) :
    N, M = map(int, input().split())
    if (N < M) :
        list_N = list(map(int, input().split()))
        list_M = list(map(int, input().split()))
    else :
        N, M = M, N
        list_M = list(map(int, input().split()))
        list_N = list(map(int, input().split()))
    max = 0
    for i in range(M - N + 1) :
        sum = 0
        for j in range(N) :
            sum += list_N[j] * list_M[j + i]
        if sum > max :
            max = sum
    print("#%d %d" % (t + 1, max))