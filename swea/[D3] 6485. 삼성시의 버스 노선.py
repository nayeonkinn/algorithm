import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for t in range(T) :
    N = int(input())

    bus = [0] * 5000
    for n in range(N) :
        route = list(map(int, input().split()))
        for i in range(route[0] - 1, route[1]) :
            bus[i] += 1

    P = int(input())
    result = [bus[int(input()) - 1] for p in range(P)]
    print(f'#{t + 1} {" ".join(map(str, result))}')