import sys
sys.stdin = open('input/5249.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())
    node = [list(map(int, input().split())) for _ in range(E)]
    node.sort(key = lambda x: x[2])
    p = [i for i in range(V + 1)]
    mst, cost = [], 0
    
    while len(mst) < V:
        n1, n2, w = node.pop(0)
        if find_set(n1) != find_set(n2):
            union(n1, n2)
            mst.append((n1, n2))
            cost += w

    print(f'#{tc} {cost}')
