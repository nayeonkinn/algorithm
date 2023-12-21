import sys
sys.stdin = open('input/1149-1.txt')  # 96, 3, 102, 208, 253

n = int(input())
rgb = [list(map(int, input().split())) for _ in range(n)]

for i in range(1, n):
    rgb[i][0] = min(rgb[i - 1][1], rgb[i - 1][2]) + rgb[i][0]
    rgb[i][1] = min(rgb[i - 1][0], rgb[i - 1][2]) + rgb[i][1]
    rgb[i][2] = min(rgb[i - 1][0], rgb[i - 1][1]) + rgb[i][2]

print(min(rgb[n - 1][0], rgb[n - 1][1], rgb[n - 1][2]))