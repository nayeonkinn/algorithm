import sys
sys.stdin = open('input/4880.txt', 'r')

def rsp(i, j):
    ii = cards[i][1]
    jj = cards[j][1]
    if ii == 1 and jj == 3:
        return i
    elif ii == 3 and jj == 1:
        return j
    else:
        return i if ii >= jj else j

def game(i, j):
    if j - i == 1:
        return cards[rsp(i, j)][0]
    elif i == j:
        return cards[i][0]
    else:
        return rsp(game(i, (i + j) // 2), game((i + j) // 2 + 1, j))

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    temp = input().split()
    cards = [(i, int(temp[i])) for i in range(N)]
    print(f'#{tc} {game(0, N - 1) + 1}')