import sys

sys.stdin = open('input/15728-2.txt')  # 10, -3

n, k = map(int, input().split())
share = sorted(map(int, input().split()))
team = list(map(int, input().split()))

for _ in range(k):
    max_t = 0
    max_val = -1e9
    for t in team:
        s = share[-1] if t > 0 else share[0]
        if t * s > max_val:
            max_t = t
            max_val = t * s
    team.remove(max_t)

print(max(i * j for i in share for j in team))