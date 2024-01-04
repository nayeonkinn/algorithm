import sys
sys.stdin = open('input/11404.txt')  # 0 2 3 1 4  12 0 15 2 5  8 5 0 1 1  10 7 13 0 3  7 4 10 6 0
input = sys.stdin.readline

n = int(input())
m = int(input())

arr = [[1e9] * n for _ in range(n)]

for i in range(n):
    arr[i][i] = 0

for _ in range(m):
    a, b, c = map(int, input().split())
    arr[a - 1][b - 1] = min(arr[a - 1][b - 1], c)  # 노선은 하나가 아닐 수 있기 때문

for i in range(n):
    for j in range(n):
        for k in range(n):
            # if j == i or k == i or j == k:  # 매번 추가 연산하는 것보다 그냥 0으로 계산되도록 하는 것이 더 빠름
            #     continue
            arr[j][k] = min(arr[j][k], arr[j][i] + arr[i][k])

for i in range(n):
    for j in range(n):
        if arr[i][j] == 1e9:
            arr[i][j] = 0
    print(*arr[i])