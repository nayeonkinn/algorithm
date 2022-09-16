import sys
sys.stdin = open('input/1486.txt')

T = int(input())
for t in range(1, T + 1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    result = sum(height)

    for i in range(1 << N):
        top = 0
        for j in range(N):
            if i & (1 << j):
                top += height[j]
        if 0 <= top - B < result:
            result = top - B

    print(f'#{t} {result}')