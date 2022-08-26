import sys
sys.stdin = open('input/6019.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    D, A, B, F = map(int, input().split())
    print(f'#{tc} {F * D / (A + B)}')