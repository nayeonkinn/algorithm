# import sys
# sys.stdin = open('input.txt', 'r')

c, r = map(int, input().split())
K = int(input())

if K > r * c :
    print(0)
else :
    seat = [[0] * c for _ in range(r)]

    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
    ji = [-1, -1, 1, 1]
    jj = [1, -1, -1, 1]

    i = j = turn = 0

    num = 1
    while True :
        while 0 <= i < r and 0 <= j < c and seat[i][j] == 0 :
            seat[i][j] = num
            if num == K :
                print(j + 1, i + 1)
                quit()
            num += 1
            i += di[turn]
            j += dj[turn]
        i += ji[turn]
        j += jj[turn]
        turn = (turn + 1) % 4