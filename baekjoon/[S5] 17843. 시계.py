import sys

sys.stdin = open('input/17843.txt')  # 50.058333
input = sys.stdin.readline

for _ in range(int(input())):
    h, m, s = map(int, input().split())
    angle = sorted([h * 30 + m * 0.5 + s * (1 / 120), m * 6 + s * 0.1, s * 6])
    print(min(angle[1] - angle[0], angle[2] - angle[1], angle[0] + 360 - angle[2]))