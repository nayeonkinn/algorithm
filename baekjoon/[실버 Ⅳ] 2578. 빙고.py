import sys
sys.stdin = open('input.txt', 'r')

def countBingo(bingo) :
    cnt = 0
    r_down = 0
    l_down = 0
    for i in range(5) :
        hor = 0
        ver = 0
        for j in range(5) :
            if bingo[5 * i + j] == 0 : # 가로
                hor += 1
            if bingo[i + 5 * j] == 0 : # 세로
                ver += 1
        if hor == 5:
            cnt += 1
        if ver == 5:
            cnt += 1

        if bingo[6 * i] == 0 : # 오른쪽 아래 대각선
            r_down += 1
        if bingo[4 * (i + 1)] == 0 : # 왼쪽 아래 대각선
            l_down += 1
    if r_down == 5 :
        cnt += 1
    if l_down == 5 :
        cnt += 1
        
    return cnt

bingo = []
answer = []
for i in range(5) :
    bingo.extend(list(map(int, input().split())))
for j in range(5) :
    answer.extend(list(map(int, input().split())))

for a in range(25) :
    for b in range(25) :
        if answer[a] == bingo[b] :
            bingo[b] = 0
            break
    if countBingo(bingo) > 2 :
        print(a + 1)
        break