import sys
sys.stdin = open('input/1265.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, P = map(int, input().split())
    candy = (N // P) ** (P - N % P) * (N // P + 1) ** (N % P)
    print(f'#{tc} {candy}')