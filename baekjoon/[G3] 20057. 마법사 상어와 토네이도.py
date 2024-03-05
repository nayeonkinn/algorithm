import sys

sys.stdin = open('input/20057-1.txt')  # 10, 85, 139, 7501, 283, 22961
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

delta = ((0, -1), (1, 0), (0, 1), (-1, 0))
left = [(-1, 1, 0.01), (1, 1, 0.01), (-2, 0, 0.02), (2, 0, 0.02), (0, -2, 0.05), (-1, 0, 0.07), (1, 0, 0.07), (-1, -1, 0.1), (1, -1, 0.1), (0, -1, 0)]
ref = [left, list((-y, x, z) for x, y, z in left), list((x, -y, z) for x, y, z in left), list((y, x, z) for x, y, z in left)]

direction = []
for i in range(1, n, 2):
    direction.extend([0] * i + [1] * i + [2] * (i + 1) + [3] * (i + 1))
direction.extend([0] * (n - 1))

answer = 0

x = y = n // 2
for d in direction:
    x, y = x + delta[d][0], y + delta[d][1]

    if sand := arr[x][y]:
        arr[x][y] = 0
        left_sand = sand

        for dx, dy, ratio in ref[d]:
            nx, ny = x + dx, y + dy

            if ratio:
                moving_sand = int(sand * ratio)
                left_sand -= moving_sand  # 모래가 격자 밖으로 이동한다고 그 모래가 알파 칸에 더해지는 것이 아니었다 0_0
            else:
                moving_sand = left_sand
            
            if 0 <= nx < n and 0 <= ny < n:
                arr[nx][ny] += moving_sand
            else:
                answer += moving_sand

print(answer)