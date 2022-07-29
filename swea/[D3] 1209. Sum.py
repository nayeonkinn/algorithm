for t in range(10) :
    input()
    array = []
    for r in range(100) :
        array.append(list(map(int, input().split())))

    maxx = 0
    cross1 = 0
    cross2 = 0
    for i in range(100) :
        row = 0
        col = 0
        cross1 += array[i][i]
        cross2 += array[i][99 - i]
        for j in range(100) :
            row += array[i][j]
            col += array[j][i]
            if max(row, col) > maxx :
                maxx = max(row, col)
        if max(cross1, cross2) > maxx :
            maxx = max(cross1, cross2)

    print(f'#{t + 1} {maxx}')