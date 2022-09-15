import sys
sys.stdin = open('input/5178.txt')

def fill(L):
    if L <= N and tree[L]:
        return tree[L]
    elif L > N:
        return 0
    return fill(2 * L) + fill(2 * L + 1)

T = int(input())
for t in range(1, T + 1):
    N, M, L = map(int, input().split())
    tree = [0] * (N + 1)
    for _ in range(M):
        node, num = map(int, input().split())
        tree[node] = num
    print(f'#{t} {fill(L)}')