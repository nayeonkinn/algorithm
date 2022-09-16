import sys
sys.stdin = open('input/1861.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    temp = [list(map(int, input().split())) for _ in range(N)]
    rooms = [(-1, -1) for _ in range(N * N + 2)]
    for i in range(N):
        for j in range(N):
            rooms[temp[i][j]] = (i, j)

    max_cnt, cnt, start = 0, 1, N * N + 1
    for i in range(1, N * N + 1):
        if abs(rooms[i][0] - rooms[i + 1][0]) + abs(rooms[i][1] - rooms[i + 1][1]) == 1:
            cnt += 1
            continue
        if max_cnt < cnt:
            max_cnt = cnt
            start = i - cnt + 1
        cnt = 1

    print(f'#{t} {start} {max_cnt}')
