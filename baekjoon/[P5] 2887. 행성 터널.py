import sys

sys.stdin = open('input/2887.txt')  # 4
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

arr = []
parent = []
edge = []

answer = 0

for i in range(n):
    x, y, z = map(int, input().split())
    arr.append((x, y, z, i))
    parent.append(i)

for i in range(3):
    arr.sort(key=lambda x: x[i])
    for j in range(n - 1):
        edge.append((abs(arr[j][i] - arr[j + 1][i]), arr[j][3], arr[j + 1][3]))

edge.sort()

for cost, a, b in edge:
    if find(a) != find(b):
        union(a, b)
        answer += cost

print(answer)