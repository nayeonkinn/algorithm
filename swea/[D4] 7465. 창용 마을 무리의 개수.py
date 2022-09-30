import sys
sys.stdin = open('input/7465.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    p = [i for i in range(N + 1)]
    for _ in range(M):
        p1, p2 = map(int, input().split())
        p[find_set(p2)] = find_set(p1)
    group = set()
    for i in p:
        group.add(find_set(i))
    print(f'#{tc} {len(group) - 1}')
