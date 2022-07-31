import sys
sys.stdin = open("input.txt", "r")

for t in range(1, 11):
    input()
    ladder = [list(map(int, input().split())) for i in range(100)]
    x_list = [j for j in range(100) if ladder[0][j] == 1]

    max_x = 0
    min_cnt = 100 * 100
    for x_start in x_list :
        x = x_start
        y = 0
        cnt = 0
        before = x, y
        
        while y < 99:
            if x != 0 and ladder[y][x - 1] == 1 and (x - 1, y) != before :
                before = x, y
                x -= 1
            elif x != 99 and ladder[y][x + 1] == 1 and (x + 1, y) != before :
                before = x, y
                x += 1
            else :
                before = x, y
                y += 1
            cnt += 1

        if cnt <= min_cnt :
            min_cnt = cnt
            max_x = x_start
    print(f'#{t} {max_x}')