import sys
sys.stdin = open('input/5248.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    p = [i for i in range(N + 1)]
    for i in range(M):
        union(arr[2 * i], arr[2 * i + 1])
    group = set()
    for i in range(1, N + 1):
        group.add(find_set(i))
    print(f'#{tc} {len(set(group))}')
