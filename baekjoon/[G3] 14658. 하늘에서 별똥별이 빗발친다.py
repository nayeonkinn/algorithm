import sys

sys.stdin = open('input/14658.txt')  # 3
input = sys.stdin.readline

n, m, l, k = map(int, input().split())
stars = [list(map(int, input().split())) for _ in range(k)]

answer = 0

for i in range(k):
    for j in range(i, k):  # 본인 포함
        cnt = 0

        sx, sy = min(stars[i][0], stars[j][0]), min(stars[i][1], stars[j][1])

        for x, y in stars:
            if sx <= x <= sx + l and sy <= y <= sy + l:
                cnt += 1

        answer = max(answer, cnt)

print(k - answer)