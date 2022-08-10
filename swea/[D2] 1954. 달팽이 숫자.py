import sys
sys.stdin = open('input.txt', 'r')

di = [0, 1, 0, -1] # 방향
dj = [1, 0, -1, 0]
ji = [1, -1, -1, 1] # 값 조정
jj = [-1, -1, 1, 1]

T = int(input())
for t in range(T) :
    N = int(input())
    snail = [[0] * N for _ in range(N)]
    i = j = turn =  0
    num = 1
    while num <= N ** 2 :
        while 0 <= i < N and 0 <= j < N and snail[i][j] == 0 :
            snail[i][j] = num
            num += 1
            i += di[turn]
            j += dj[turn]
        i += ji[turn]
        j += jj[turn]
        turn = (turn + 1) % 4

    print(f'#{t + 1}')
    for row in range(N) :
        print(" ".join(map(str, snail[row])))