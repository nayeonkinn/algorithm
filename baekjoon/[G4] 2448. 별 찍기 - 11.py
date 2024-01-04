def star(size, x, y):
    if size == 3:
        for rx, ry in rule:
            stars[x + rx][y + ry] = '*'
    else:
        star(size//2, x, y + size//2)
        star(size//2, x + size//2, y)
        star(size//2, x + size//2, y + size)

n = int(input())

stars = [[' '] * (2 * n) for _ in range(n)]
rule = ((0, 2), (1, 1), (1, 3), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4))

star(n, 0, 0)

for star in stars:
    print("".join(star))