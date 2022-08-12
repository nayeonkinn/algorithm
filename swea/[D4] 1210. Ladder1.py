for t in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for _ in range(100)]
    y = 99
    x = ladder[y].index(2)
    before = x, y
    while y > 0:
        if x != 0 and ladder[y][x - 1] == 1 and (x - 1, y) != before :
            before = x, y
            x -= 1
        elif x != 99 and ladder[y][x + 1] == 1 and (x + 1, y) != before :
            before = x, y
            x += 1
        else :
            before = x, y
            y -= 1
    print(f'#{t} {x}')