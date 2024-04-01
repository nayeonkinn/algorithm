import sys

sys.stdin = open('input/1976.txt')  # YES
input = sys.stdin.readline

def union(a, b):
    a = find(a)
    b = find(b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

def find(a):
    if parent[a] != a:
        parent[a] = find(parent[a])
    return parent[a]

n = int(input())
m = int(input())
adj = [list(map(int, input().split())) for _ in range(n)]
plan = list(map(lambda x: int(x) - 1, input().split()))

parent = [i for i in range(n)]

for i in range(n):
    for j in range(i + 1, n):
        if adj[i][j]:
            union(i, j)

if len(set(find(p) for p in plan)) == 1:
    print('YES')
else:
    print('NO')