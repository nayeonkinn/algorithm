import sys
sys.stdin = open('input/4864.txt', 'r')

T = int(input())
for tc in range(T):
    p = input()
    t = input()
    compare = 0

    i = j = 0
    while i < len(t) and j < len(p):
        if t[i] != p[j]:
            i -= j
            j = -1
        if j == len(p) - 1:
            compare = 1
            break
        i += 1
        j += 1

    print(f'#{tc + 1} {compare}')