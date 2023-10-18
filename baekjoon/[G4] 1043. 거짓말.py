import sys
sys.stdin = open('input/1043-1.txt')  # 3, 0, 1, 2, 4, 5, 0, 0


def union(x, y):
    x = get_parent(x)
    y = get_parent(y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y


def get_parent(x):
    if parent[x] == x:
        return x
    return get_parent(parent[x])


def find(x, y):
    if get_parent(x) == get_parent(y):
        return True
    return False


n, m = map(int, input().split())
_, *truth = list(map(int, input().split()))
parties = [list(map(int, input().split())) for _ in range(m)]
parent = [i for i in range(n + 1)]

for t in truth:
    union(t, 0)

for cnt, *party in parties:
    if cnt == 1:
        continue

    for p in party[1:]:
        union(p, party[0])

answer = 0
for cnt, *party in parties:
    story = False
    for p in party:
        if find(p, 0):
            story = True
            break
    
    if not story:
        answer += 1

print(answer)
