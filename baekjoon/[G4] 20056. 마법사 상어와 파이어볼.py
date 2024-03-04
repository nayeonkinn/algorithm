import sys
from collections import defaultdict

sys.stdin = open('input/20056-1.txt')  # 8, 8, 0, 9
input = sys.stdin.readline

N, M, K = map(int, input().split())

fireballs = []
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    fireballs.append((r - 1, c - 1, m, s, d))

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

for _ in range(K):
    grid = defaultdict(list)
    for r, c, m, s, d in fireballs:
        nx, ny = (r + dx[d] * s) % N, (c + dy[d] * s) % N
        grid[(nx, ny)].append((m, s, d))
    
    fireballs = []
    for rc, fs in grid.items():
        if len(fs) > 1:
            m = sum([f[0] for f in fs]) // 5
            if not m:
                continue
            s = sum([f[1] for f in fs]) // len(fs)
            odd = [f[2] % 2 for f in fs]
            fireballs.extend([(*rc, m, s, d) for d in range(0 if all(odd) or not any(odd) else 1, 8, 2)])
        else:
            fireballs.append((*rc, *fs[0]))

print(sum([f[2] for f in fireballs]))