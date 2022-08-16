import sys
sys.stdin = open('input/1979.txt', 'r')

T = int(input())
for t in range(T) :
    N, K = map(int, input().split())
    puzzle = []
    for n in range(N) :
        puzzle.append(list(map(int, input().split())))
    cnt = 0
    for i in range(N) :
        row = 0
        col = 0
        for j in range(N) :
            if puzzle[i][j] == 1 :
                row += 1
            else :
                if row == K :
                    cnt += 1
                row = 0
            if puzzle[j][i] == 1 :
                col += 1
            else :
                if col == K :
                    cnt += 1
                col = 0
        if row == K :
            cnt += 1
        if col == K :
            cnt += 1
    print("#%d %d" % (t + 1, cnt))