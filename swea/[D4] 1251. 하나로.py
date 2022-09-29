import sys
sys.stdin = open('input/1251.txt')

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    p[find_set(y)] = find_set(x)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))
    E = float(input())

    distance = []
    for i in range(N):
        for j in range(i + 1, N):
            d = ((X[i] - X[j]) ** 2 + (Y[i] - Y[j]) ** 2) * E
            distance.append([d, i, j])
    distance.sort()
    
    cnt, cost = 0, 0
    p = [i for i in range(N)]
    for d, i, j in distance:
        if find_set(i) != find_set(j):
            cnt += 1
            cost += d
            union(i, j)
            if cnt == N - 1:
                break

    print(f'#{tc} {round(cost)}')
