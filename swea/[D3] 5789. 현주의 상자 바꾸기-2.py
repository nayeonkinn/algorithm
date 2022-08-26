import sys
sys.stdin = open('input/5789.txt', 'r')

T = int(input())
for tc in range(1, T + 1):
    N, Q = map(int, input().split())
    box = [0] * N
    for q in range(Q):
        L, R = map(int, input().split())
        for i in range(L - 1, R):
            box[i] = q + 1
    print(f'#{tc}', *box)