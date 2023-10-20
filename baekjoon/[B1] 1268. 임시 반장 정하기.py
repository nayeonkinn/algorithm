import sys
sys.stdin = open('input/1268.txt')  # 4
input = sys.stdin.readline

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
same = [[0] * N for _ in range(N)]

for grade in range(5):
    for i in range(N - 1):
        for j in range(i + 1, N):
                if info[i][grade] == info[j][grade]:
                    same[i][j] = 1
                    same[j][i] = 1

same = [sum(i) for i in same]
print(same.index(max(same)) + 1)
