import sys
sys.stdin = open('input/1860-2.txt', 'r')

def possible(waiting):
    fish = 0
    for i in range(max(temp) + 1):
        if i != 0 and i % M == 0:
            fish += K
        fish -= waiting[i]
        if fish < 0:
            return 'Impossible'
    else:
        return 'Possible'

T = int(input())
for tc in range(1, T + 1):
    N, M, K = map(int, input().split())
    temp = list(map(int, input().split()))
    waiting = [0] * (max(temp) + 1)
    for i in range(N):
        waiting[temp[i]] = 1
    print(f'#{tc} {possible(waiting)}')