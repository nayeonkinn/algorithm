import sys
sys.stdin = open('input/5174.txt')

def preorder(N):
    if not N:
        return 0
    return 1 + preorder(ch1[N]) + preorder(ch2[N])

T = int(input())
for t in range(1, T + 1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    ch1, ch2 = [0] * (E + 2), [0] * (E + 2)

    for i in range(E):
        p, c = node[2 * i], node[2 * i + 1]
        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    print(f'#{t} {preorder(N)}')