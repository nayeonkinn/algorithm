import sys
sys.stdin = open('input/8911.txt') # 2\n0\n9
input = sys.stdin.readline

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

T = int(input())
for _ in range(T):
    command = input()
    x = y = d = top = bottom = left = right = 0

    for c in command:
        if c == 'F':
            x += dx[d]
            y += dy[d]
        elif c == 'B':
            x -= dx[d]
            y -= dy[d]
        elif c == 'L':
            d = (d - 1) % 4
        elif c == 'R':
            d = (d + 1) % 4

        if x > top:
            top = x
        elif x < bottom:
            bottom = x
        if y > right:
            right = y
        elif y < left:
            left = y

    print(abs(top - bottom) * abs(left - right))
