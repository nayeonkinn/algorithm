import sys
sys.stdin = open('input/5688.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    candidate = int(N ** (1/3))
    for i in range(candidate - 1, candidate + 2):
        if i ** 3 == N:
            result = i
            break
        result = -1
    print(f'#{t} {result}')