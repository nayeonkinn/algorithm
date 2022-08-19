import sys
sys.stdin = open('input/1018-1.txt', 'r') # 1, 12, 0

def check(chess):
    cnt = 0
    for i in range(8):
        for j in range(8):
            if (i + j) % 2 == 0 and chess[i][j] != 'W':
                cnt += 1
            elif (i + j) % 2 == 1 and chess[i][j] != 'B':
                cnt += 1
            # if chess[i][j] != 'WB'[(i + j) % 2]: # 한번에 표현도 가능
            #     cnt += 1
    return cnt if cnt <= 32 else 64 - cnt

N, M = map(int, input().split())
board = [input() for _ in range(N)]

mincnt = 64
for i in range(N - 7):
    for j in range(M - 7):
        chess = [board[k][j:j + 8] for k in range(i, i + 8)]
        mincnt = min(check(chess), mincnt)
print(mincnt)