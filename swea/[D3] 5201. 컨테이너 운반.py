import sys
sys.stdin = open('input/5201.txt')

T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    W = sorted(list(map(int, input().split())), reverse = True)
    T = sorted(list(map(int, input().split())), reverse = True)

    answer = 0
    next = 0
    for i in range(M):
        for j in range(next, N):
            if T[i] >= W[j]:
                answer += W[j]
                next = j + 1
                break

    print(f'#{t} {answer}')
